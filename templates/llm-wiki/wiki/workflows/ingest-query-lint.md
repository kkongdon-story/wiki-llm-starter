# Ingest Query Lint

type: workflow
workflow_id: ingest_query_lint

## One-line Definition

Ingest, query, and lint are the three repeatable operations that keep an LLM Wiki useful.

## Summary

Ingest adds new sources. Query answers questions from the compiled wiki. Lint checks structure, source grounding, stale claims, contradiction candidates, and ontology consistency.

## Source Links

- [[sources/karpathy-llm-wiki-post]]

## Related Pages

- [[concepts/llm-wiki]]
- [[concepts/ontology-layer]]

## Open Questions

- How often should lint run for a personal wiki?
- Which lint warnings should block publishing?
