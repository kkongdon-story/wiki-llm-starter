# Project Memory

type: concept
concept_id: project_memory

## One-line Definition

Project memory는 특정 프로젝트의 규칙, 선호, 운영 맥락을 매 세션에 다시 주입해 지속성을 만드는 고정 문맥이다.

## Summary

[[sources/llm-memory-illusion-ai-memory]]는 개발자와 AI agent가 사용하는 permanent project memory를 설명한다. 이런 기억은 모델 내부에 저장되는 것이 아니라, 프로젝트 규칙 파일이나 skill 파일처럼 매 세션 앞부분에 다시 포함되는 문맥이다.

이 방식은 일반 대화 기록보다 안정적이다. 프로젝트 운영 규칙, 사용자 선호, 코드베이스 계약, 반복 워크플로우처럼 매번 유지되어야 하는 내용은 project memory에 두는 편이 좋다.

이 저장소의 `CLAUDE.md`, `AGENTS.md`, skill 파일들은 project memory에 가까운 역할을 한다.

## Source Links

- [[sources/llm-memory-illusion-ai-memory]]

## Related Pages

- [[concepts/llm-memory]]
- [[concepts/context-window]]
- [[concepts/llm-wiki]]
- [[workflows/manage-ai-memory]]

## Open Questions

- 이 LLM Wiki에서 project memory로 고정할 내용과 wiki에 축적할 내용을 어떻게 나눌 것인가?
