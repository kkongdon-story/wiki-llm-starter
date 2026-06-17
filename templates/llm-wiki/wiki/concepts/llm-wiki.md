# LLM Wiki

type: concept
concept_id: llm_wiki

## One-line Definition

An LLM Wiki is a persistent Markdown knowledge base that an AI reads, writes, links, and maintains.

## Summary

The key difference from RAG is accumulation. RAG retrieves source chunks at query time. LLM Wiki compiles useful knowledge into reusable pages before the next query.

[[sources/llm-memory-illusion-ai-memory]] adds a memory-management lens: an LLM Wiki can act like a deliberate, inspectable long-term memory layer because important knowledge is saved as Markdown pages with source links instead of relying only on hidden memory facts or the current [[concepts/context-window]].

## Source Links

- [[sources/karpathy-llm-wiki-post]]
- [[sources/llm-memory-illusion-ai-memory]]

## Related Pages

- [[concepts/ontology-layer]]
- [[concepts/llm-memory]]
- [[concepts/external-memory]]
- [[workflows/ingest-query-lint]]

## Open Questions

- What is the smallest schema that keeps quality high?
- Which ontology relations are useful enough to formalize?
