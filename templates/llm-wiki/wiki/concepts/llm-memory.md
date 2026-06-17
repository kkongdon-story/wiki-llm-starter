# LLM Memory

type: concept
concept_id: llm_memory

## One-line Definition

LLM memory는 모델이 실제로 기억을 저장한다는 뜻이 아니라, 현재 컨텍스트와 외부 저장소가 결합되어 기억처럼 보이는 작동 방식을 말한다.

## Summary

[[sources/llm-memory-illusion-ai-memory]]는 LLM이 기본적으로 이전 세션의 내용을 스스로 기억하지 않는다고 설명한다. 모델은 현재 요청에 포함된 텍스트를 읽고 다음 토큰을 예측할 뿐이며, 대화가 이어지는 느낌은 이전 메시지들이 다시 입력되기 때문에 생긴다.

따라서 LLM memory는 한 가지 기능이 아니라 여러 층의 조합으로 이해하는 편이 안전하다.

- [[concepts/context-window]]: 지금 모델에게 보이는 단기 문맥
- 요약: 오래된 문맥을 압축해 유지하는 방식
- [[concepts/external-memory]]: 별도 저장소에서 관련 사실을 다시 넣는 장기 기억 방식
- [[concepts/project-memory]]: 프로젝트 규칙이나 선호를 매 세션 앞부분에 주입하는 고정 기억

## Source Links

- [[sources/llm-memory-illusion-ai-memory]]

## Related Pages

- [[concepts/context-window]]
- [[concepts/external-memory]]
- [[concepts/project-memory]]
- [[workflows/manage-ai-memory]]
- [[concepts/llm-wiki]]

## Open Questions

- 개인 지식 시스템에서 LLM memory와 LLM Wiki의 역할을 어디까지 분리해야 하는가?
