# External Memory

type: concept
concept_id: external_memory

## One-line Definition

External memory는 대화 밖 저장소에 사실을 보관했다가, 관련 질문이 들어올 때 다시 프롬프트에 넣어주는 장기 기억 방식이다.

## Summary

[[sources/llm-memory-illusion-ai-memory]]는 external memory를 context window와 구분한다. Context window가 현재 대화의 단기 문맥이라면, external memory는 세션을 넘어 살아남는 장기 저장소에 가깝다.

대표 방식은 중요한 사실을 추출해 [[entities/vector-database]] 같은 별도 저장소에 저장하고, 사용자의 다음 요청과 관련 있을 때 그 사실을 다시 프롬프트에 주입하는 것이다. 이 구조 때문에 AI가 "나를 기억한다"고 느껴질 수 있다.

LLM Wiki도 이 개념과 닮아 있다. 다만 LLM Wiki는 단순 자동 기억 저장소가 아니라, 사람이 검토할 수 있는 Markdown 페이지와 출처 링크를 통해 지식을 축적한다.

## Source Links

- [[sources/llm-memory-illusion-ai-memory]]

## Related Pages

- [[concepts/llm-memory]]
- [[concepts/context-window]]
- [[concepts/llm-wiki]]
- [[entities/vector-database]]

## Open Questions

- 어떤 사용자 사실은 external memory에 저장하고, 어떤 사실은 wiki page로만 남기는 것이 좋은가?
