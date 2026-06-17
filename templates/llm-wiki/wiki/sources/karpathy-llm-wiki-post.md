# Karpathy LLM Wiki Post

type: source
source_id: karpathy_llm_wiki_post

## One-line Definition

Karpathy's LLM Wiki idea describes an LLM-maintained Markdown knowledge base that compounds over time.

## Summary

The source argues that raw documents should be compiled into a persistent wiki instead of being retrieved from scratch for every question.

The useful pattern is:

- raw sources stay immutable
- the LLM writes and maintains the wiki
- Obsidian works as the viewer or IDE
- linting keeps the knowledge base healthy

## Source Links

- Related concept: [[concepts/llm-wiki]]
- Related workflow: [[workflows/ingest-query-lint]]

## Extracted Claims

- LLM-maintained wiki pages can accumulate knowledge across sessions.
- A source can update many existing pages instead of creating one isolated summary.
- Health checks should find contradictions, stale claims, orphan pages, and missing links.

## Open Questions

- Which parts should stay Markdown-only?
- When should a larger system add RAG or a graph database?
