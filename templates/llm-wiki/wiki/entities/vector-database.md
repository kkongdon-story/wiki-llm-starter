# Vector Database

type: entity
entity_id: vector_database

## One-line Definition

Vector database는 텍스트나 사실을 벡터 형태로 저장해, 관련 질문이 들어왔을 때 비슷한 정보를 다시 찾는 저장소다.

## Summary

[[sources/llm-memory-illusion-ai-memory]]는 external memory의 대표 구현으로 vector database를 언급한다. 대화에서 중요한 사실을 추출해 외부 저장소에 넣고, 이후 관련 요청이 들어오면 그 사실을 프롬프트에 다시 넣는 식이다.

이 위키에서는 vector database를 LLM memory의 한 구현 도구로 기록하되, 아직 실제 시스템 구성 요소로 채택했다는 의미는 아니다.

## Source Links

- [[sources/llm-memory-illusion-ai-memory]]

## Related Pages

- [[concepts/external-memory]]
- [[concepts/llm-memory]]

## Open Questions

- 이 LLM Wiki가 Markdown만으로 충분한지, 나중에 vector database가 필요한지 판단할 기준은 무엇인가?
