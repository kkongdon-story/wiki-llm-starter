# Personal LLM Wiki Rules

You are maintaining this vault as an LLM Wiki.

## Mission

Compile raw sources into a persistent Markdown wiki and an ontology-backed knowledge system. Do not treat this as a one-time summary task.

## Layers

- `raw/`: source of truth. Read-only except for optional processed markers.
- `wiki/`: LLM-maintained pages for sources, concepts, entities, workflows, and questions.
- `schema/`: writing and maintenance rules.
- `ontology/`: T-Box, A-Box, and starter inference rules.

## Ingest Checklist

1. Read the new source.
2. Create or update a source summary under `wiki/sources/`.
3. Update relevant pages under `wiki/concepts/`, `wiki/entities/`, and `wiki/workflows/`.
4. Add instances/facts to `ontology/abox.json`.
5. Run:

```text
python ../../scripts/ontology_reasoner.py --root .
python ../../scripts/lint_wiki.py --root .
```

6. Append `log.md` with changed files, uncertainties, and next questions.
7. Sync updated wiki pages to gbrain (only after steps 5–6 pass):

```text
gbrain import wiki/
```

## Query Checklist

0. Get relevant page paths from gbrain (path hints only — do not use as answer):

```text
gbrain search "<question>"
```

Use the returned paths to decide which wiki pages to read first. Do not treat gbrain output as the final answer.

1. Start from `wiki/index.md`.
2. Read the most relevant wiki pages before raw sources.
3. Answer with clear source references.
4. Save reusable answers under `wiki/questions/`.

## Lint Checklist

1. Find orphan pages.
2. Find source-less claims.
3. Find stale claims.
4. Find contradiction candidates.
5. Run ontology reasoner and fix errors.

## Writing Style

- Keep pages short and link-rich.
- Use `[[folder/page-id]]` links.
- Prefer stable English IDs and Korean labels.
- Separate confirmed facts, inference, and open questions.
