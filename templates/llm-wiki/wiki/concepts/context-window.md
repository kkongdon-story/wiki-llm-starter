# Context Window

type: concept
concept_id: context_window

## One-line Definition

Context window는 LLM이 한 번의 응답을 만들 때 실제로 볼 수 있는 입력 텍스트의 범위다.

## Summary

[[sources/llm-memory-illusion-ai-memory]]는 context window를 AI의 단기 기억에 비유한다. 사용자가 두 번째 메시지를 보내면 시스템은 새 메시지만 보내는 것이 아니라, 이전 사용자 메시지와 AI 답변을 함께 묶어 LLM에게 다시 보낸다.

중요한 점은 LLM이 대화를 저장해두고 떠올리는 것이 아니라, 현재 context window 안의 텍스트를 빠르게 다시 읽는다는 점이다. 어떤 사실이 이 범위 안에 없으면 모델은 그 사실을 직접 볼 수 없다.

Context window에는 토큰 한계가 있다. 대화가 길어지면 오래된 내용이 밀려나거나, 요약되거나, 외부 메모리에서 일부 사실만 다시 주입될 수 있다.

## Source Links

- [[sources/llm-memory-illusion-ai-memory]]

## Related Pages

- [[concepts/llm-memory]]
- [[concepts/external-memory]]
- [[concepts/project-memory]]

## Open Questions

- 이 위키에서 긴 raw 자료를 ingest할 때 context window 한계를 어떻게 다룰 것인가?
