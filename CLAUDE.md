# LLM Wiki Operating Rules

Use these rules when maintaining this repository or a copied `templates/llm-wiki` vault.

## Goal

Build and maintain an LLM Wiki that compiles raw sources into a persistent, interlinked Markdown knowledge base with an ontology layer. This is not a one-shot summary workflow and not a simple RAG cache.

## Folder Contract

- `raw/` is immutable source material. Read it, cite it, and mark processed state only when the local workflow explicitly allows it.
- `wiki/` is the LLM-maintained knowledge layer. Write summaries, concept pages, entity pages, question pages, and synthesis pages here.
- `schema/` defines how the LLM should write and maintain the wiki.
- `ontology/tbox.json` defines the domain vocabulary: classes, relations, domain/range, and disjointness.
- `ontology/abox.json` stores actual instances and facts extracted from sources.
- `ontology/inference-rules.json` stores explicit starter inference rules.
- `log.md` records ingest/query/lint actions.

## Core Operations

### Ingest

When new material enters `raw/`:

1. Identify source type, author/date if available, topic, and reliability limits.
2. Create or update a source summary page in `wiki/sources/`.
3. Update related concept/entity/workflow pages instead of always creating new pages.
4. Add or update A-Box instances and facts in `ontology/abox.json`.
5. Run ontology validation and record errors before claiming completion.
6. Append `log.md` with what changed and what remains uncertain.

### Query

When answering a question:

1. Use `wiki/index.md`, related wiki pages, and ontology facts before reading every raw source.
2. Cite the relevant wiki/source pages in the answer.
3. If the answer creates durable insight, save it as a new or updated wiki page.
4. Do not silently fill gaps. Name uncertainty and propose the next source needed.

### Lint

Regularly check:

1. Orphan wiki pages with no incoming or outgoing links.
2. Claims without source links.
3. Contradictory claims.
4. Stale pages whose source version/date is older than the domain needs.
5. Ontology errors: missing classes, missing relations, domain/range violations, disjoint-class conflicts.

## Ontology Rules

- Keep T-Box and A-Box separate.
- Do not add a relation without `domain` and `range`.
- Use stable IDs in English snake_case.
- Use Korean labels for human-facing display.
- If a relation feels vague, use a plain Markdown note first and add the formal relation only after it is useful twice.
- Prefer a small accurate ontology over a large speculative one.

## Simplicity Rules

- Add the smallest structure that makes the next ingest/query/lint safer.
- Do not create enterprise graph infrastructure before the Markdown workflow is useful.
- Do not delete raw sources.
- Do not rewrite unrelated wiki pages just because they look imperfect.

## Verification

Before saying the system is ready:

```text
python scripts/ontology_reasoner.py --root templates/llm-wiki
python scripts/lint_wiki.py --root templates/llm-wiki
```

If Python is not on PATH, use the local machine's available Python executable and report the exact command used.
