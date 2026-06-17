#!/usr/bin/env python3
"""Small ontology validator and starter reasoner for the LLM Wiki template."""

from __future__ import annotations

import argparse
import json
from collections import defaultdict
from pathlib import Path
from typing import Any


Fact = tuple[str, str, str]


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as file:
        return json.load(file)


def closure_for(class_id: str, parents: dict[str, list[str]]) -> set[str]:
    seen: set[str] = set()
    stack = [class_id]
    while stack:
        current = stack.pop()
        if current in seen:
            continue
        seen.add(current)
        stack.extend(parents.get(current, []))
    return seen


def is_a(actual: str, expected: str, parents: dict[str, list[str]]) -> bool:
    return expected in closure_for(actual, parents)


def infer_rule_facts(facts: set[Fact], rules: list[dict[str, Any]]) -> list[tuple[Fact, str]]:
    inferred: list[tuple[Fact, str]] = []

    for rule in rules:
        premises = rule.get("if", [])
        conclusion = rule.get("then", {})
        if len(premises) != 2:
            continue

        first_matches = [fact for fact in facts if fact[1] == premises[0].get("relation")]
        second_matches = [fact for fact in facts if fact[1] == premises[1].get("relation")]

        for first in first_matches:
            for second in second_matches:
                bindings: dict[str, str] = {}
                if not bind_fact(premises[0], first, bindings):
                    continue
                if not bind_fact(premises[1], second, bindings):
                    continue
                inferred_fact = resolve_fact(conclusion, bindings)
                if inferred_fact and inferred_fact not in facts:
                    inferred.append((inferred_fact, rule.get("id", "unnamed_rule")))

    return inferred


def bind_fact(pattern: dict[str, str], fact: Fact, bindings: dict[str, str]) -> bool:
    keys = ["subject", "relation", "object"]
    for value, key in zip(fact, keys):
        expected = pattern.get(key)
        if expected is None:
            continue
        if expected.startswith("?"):
            previous = bindings.get(expected)
            if previous is not None and previous != value:
                return False
            bindings[expected] = value
        elif expected != value:
            return False
    return True


def resolve_fact(pattern: dict[str, str], bindings: dict[str, str]) -> Fact | None:
    values: list[str] = []
    for key in ["subject", "relation", "object"]:
        value = pattern.get(key)
        if value is None:
            return None
        values.append(bindings.get(value, value) if value.startswith("?") else value)
    return (values[0], values[1], values[2])


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate and reason over a starter LLM Wiki ontology.")
    parser.add_argument("--root", default=".", help="Wiki root that contains ontology/")
    args = parser.parse_args()

    root = Path(args.root)
    ontology_dir = root / "ontology"
    tbox = load_json(ontology_dir / "tbox.json")
    abox = load_json(ontology_dir / "abox.json")
    rules = load_json(ontology_dir / "inference-rules.json").get("rules", [])

    classes = {item["id"]: item for item in tbox.get("classes", [])}
    relations = {item["id"]: item for item in tbox.get("relations", [])}
    parents = {class_id: data.get("subClassOf", []) for class_id, data in classes.items()}

    errors: list[str] = []
    inferred_types: dict[str, set[str]] = defaultdict(set)

    for class_id, parent_ids in parents.items():
        for parent_id in parent_ids:
            if parent_id not in classes:
                errors.append(f"class '{class_id}' references missing parent class '{parent_id}'")

    for relation_id, relation in relations.items():
        for key in ["domain", "range"]:
            if relation.get(key) not in classes:
                errors.append(f"relation '{relation_id}' has missing {key} class '{relation.get(key)}'")

    instance_types: dict[str, set[str]] = defaultdict(set)
    for instance in abox.get("instances", []):
        instance_id = instance["id"]
        for class_id in instance.get("types", []):
            if class_id not in classes:
                errors.append(f"instance '{instance_id}' uses missing class '{class_id}'")
                continue
            instance_types[instance_id].add(class_id)
            instance_types[instance_id].update(closure_for(class_id, parents))

    instance_ids = set(instance_types)
    facts: set[Fact] = set()
    for fact in abox.get("facts", []):
        subject = fact["subject"]
        relation_id = fact["relation"]
        obj = fact["object"]
        facts.add((subject, relation_id, obj))

        if subject not in instance_ids:
            errors.append(f"fact subject '{subject}' is not defined as an instance")
        if obj not in instance_ids:
            errors.append(f"fact object '{obj}' is not defined as an instance")
        if relation_id not in relations:
            errors.append(f"fact relation '{relation_id}' is not defined in T-Box")
            continue

        relation = relations[relation_id]
        domain = relation["domain"]
        range_ = relation["range"]

        if subject in instance_types and not any(is_a(t, domain, parents) for t in instance_types[subject]):
            errors.append(f"domain violation: '{subject}' --{relation_id}--> '{obj}' expects subject type '{domain}'")
        if obj in instance_types and not any(is_a(t, range_, parents) for t in instance_types[obj]):
            errors.append(f"range violation: '{subject}' --{relation_id}--> '{obj}' expects object type '{range_}'")

        inferred_types[subject].add(domain)
        inferred_types[obj].add(range_)

        inverse = relation.get("inverseOf")
        if inverse:
            facts.add((obj, inverse, subject))

    for instance_id, types in instance_types.items():
        expanded_types = set(types)
        for type_id in list(types):
            expanded_types.update(closure_for(type_id, parents))
        for type_id in expanded_types:
            for disjoint in classes[type_id].get("disjointWith", []):
                if disjoint in expanded_types:
                    errors.append(f"disjoint-class conflict: '{instance_id}' has both '{type_id}' and '{disjoint}'")

    rule_inferences = infer_rule_facts(facts, rules)

    print("Ontology reasoner report")
    print(f"- root: {root}")
    print(f"- classes: {len(classes)}")
    print(f"- relations: {len(relations)}")
    print(f"- instances: {len(instance_ids)}")
    print(f"- asserted facts: {len(abox.get('facts', []))}")
    print(f"- inferred type hints: {sum(len(v) for v in inferred_types.values())}")
    print(f"- inferred facts: {len(rule_inferences)}")

    if rule_inferences:
        print("\nInference examples")
        for (subject, relation_id, obj), rule_id in rule_inferences[:10]:
            print(f"- {subject} --{relation_id}--> {obj}  [by {rule_id}]")

    if errors:
        print("\nErrors")
        for error in errors:
            print(f"- {error}")
        return 1

    print("\nOK: ontology is consistent for the starter reasoner.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
