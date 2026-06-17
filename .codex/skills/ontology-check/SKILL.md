---
name: ontology-check
description: Validate T-Box, A-Box, relation domain/range, and starter inference examples for an LLM Wiki ontology.
---

# ontology-check

Use this skill when the user asks to check ontology, T-Box, A-Box, domain/range, reasoner, or inference results.

Korean triggers include:

- `온톨로지 검사해줘`
- `T-Box A-Box 맞는지 봐줘`
- `domain range 오류 확인해줘`
- `reasoner 돌려줘`
- `추론 예시 설명해줘`

## Goal

Make the ontology understandable and trustworthy. The user should know not only whether the check passed, but also what the inference means.

## Inputs

- `ontology/tbox.json`
- `ontology/abox.json`
- `ontology/inference-rules.json`
- `scripts/ontology_reasoner.py`

## Workflow

1. Read T-Box:
   - classes
   - subclass relationships
   - disjoint classes
   - relations
   - domain/range
2. Read A-Box:
   - instances
   - facts
3. Run:

```text
C:\Python313\python.exe scripts\ontology_reasoner.py --root <vault>
```

4. Classify errors:
   - class problem
   - relation problem
   - domain/range problem
   - fact problem
   - inference rule problem
5. Explain inference examples in plain Korean.

## Plain Explanation Pattern

Use this shape:

```text
원문 A가 개념 B를 언급했고,
위키 페이지 C가 원문 A에서 파생됐다면,
reasoner는 C도 B와 관련 있다고 추론합니다.
```

## Output

Report:

- pass/fail
- class count
- relation count
- instance count
- fact count
- inferred facts
- plain-language explanation
- fix suggestions

