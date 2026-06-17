# Manage AI Memory

type: workflow
workflow_id: manage_ai_memory

## One-line Definition

Manage AI memory는 AI가 무엇을 단기 문맥으로 보고, 무엇을 장기 기억으로 다시 불러오게 할지 사용자가 의도적으로 정하는 운영 흐름이다.

## Summary

[[sources/llm-memory-illusion-ai-memory]]는 사용자가 AI의 memory facts를 관리할 수 있다고 설명한다. 대화 기록은 과거 채팅 목록이고, memory facts는 이후 답변 개인화에 다시 주입될 수 있는 추출된 사실이다.

실무 흐름은 다음처럼 정리할 수 있다.

1. 현재 작업에 필요한 내용은 [[concepts/context-window]] 안에 명시한다.
2. 반복해서 필요한 규칙과 선호는 [[concepts/project-memory]]에 둔다.
3. 세션을 넘어 유지할 사실은 [[concepts/external-memory]] 또는 LLM Wiki에 저장한다.
4. 오래되었거나 민감한 memory facts는 설정에서 확인하고 삭제한다.
5. 출처와 검토가 필요한 지식은 자동 memory가 아니라 `wiki/` 페이지로 남긴다.

## Source Links

- [[sources/llm-memory-illusion-ai-memory]]

## Related Pages

- [[concepts/llm-memory]]
- [[concepts/context-window]]
- [[concepts/external-memory]]
- [[concepts/project-memory]]
- [[entities/vector-database]]

## Open Questions

- 개인 운영에서는 어떤 사실을 자동 memory보다 LLM Wiki에 우선 저장해야 하는가?
