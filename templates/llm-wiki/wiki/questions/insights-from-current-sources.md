# Insights From Current Sources

type: question
question_id: insights_from_current_sources
status: answered
source: [[sources/karpathy-llm-wiki-post]], [[sources/llm-memory-illusion-ai-memory]]

## One-line Definition

현재 위키 자료가 주는 핵심 통찰은 AI를 "기억하는 존재"로 믿기보다, 기억이 남도록 구조를 설계해야 한다는 것이다.

## Summary

현재 들어간 자료는 두 가지를 함께 말한다. [[sources/karpathy-llm-wiki-post]]는 raw 자료를 매번 다시 검색하는 대신, LLM이 읽고 정리한 지식을 Markdown wiki로 누적해야 한다고 설명한다. [[sources/llm-memory-illusion-ai-memory]]는 LLM의 기억이 실제 생물학적 기억이 아니라 [[concepts/context-window]], 요약, [[concepts/external-memory]], [[concepts/project-memory]]의 조합이라고 설명한다.

따라서 사용자가 얻을 수 있는 실전 통찰은 다음과 같다.

1. AI가 중요한 것을 알아서 기억할 거라고 기대하면 안 된다. 중요한 맥락은 [[concepts/context-window]] 안에 직접 넣거나, [[concepts/project-memory]]나 LLM Wiki에 남겨야 한다.
2. LLM Wiki는 단순 노트 앱이 아니라, AI의 장기 기억을 사람이 볼 수 있는 형태로 만든 장치다.
3. 숨겨진 memory facts보다 출처가 달린 Markdown 페이지가 더 검토 가능하고 수정 가능하다.
4. 좋은 지식 시스템은 원본, 요약, 개념, 관계, 작업 로그를 분리한다. 이 분리가 나중에 오류 수정과 재사용을 쉽게 만든다.
5. 지금 단계에서는 거대한 RAG나 graph database보다, 작은 wiki와 검증 가능한 ontology가 먼저다.

## Source Links

- [[sources/karpathy-llm-wiki-post]]
- [[sources/llm-memory-illusion-ai-memory]]

## Related Pages

- [[concepts/llm-wiki]]
- [[concepts/llm-memory]]
- [[concepts/context-window]]
- [[concepts/external-memory]]
- [[concepts/project-memory]]
- [[workflows/manage-ai-memory]]

## Answer

이 위키가 지금 주는 가장 큰 통찰은 "AI에게 기억을 맡기지 말고, 기억이 작동하는 환경을 설계하라"는 것이다.

AI는 대화 내용을 마음속에 저장해두는 존재가 아니다. 현재 보이는 문맥을 읽고 답한다. 그래서 중요한 내용이 컨텍스트에서 밀려나면 잊은 것처럼 행동한다. 반대로 중요한 규칙과 사실을 프로젝트 메모리나 LLM Wiki에 잘 남겨두면, AI는 훨씬 일관된 파트너처럼 작동한다.

여기서 LLM Wiki의 의미가 생긴다. LLM Wiki는 AI의 숨겨진 기억을 믿는 방식이 아니라, 원본과 출처가 있는 지식을 Markdown으로 누적하는 방식이다. 즉, 사용자가 직접 검토하고 고칠 수 있는 장기 기억이다.

초기 운영 원칙은 단순하다. 원본은 `raw/`에 보존하고, 반복해서 쓸 지식은 `wiki/`에 정리하고, 정말 구조화할 가치가 생긴 개념과 관계만 `ontology/`에 넣는다. 그리고 작업 내역은 `log.md`에 남긴다.

## Open Questions

- 나에게 중요한 project memory는 무엇이고, 단순 참고 자료로만 남길 source summary는 무엇인가?
- 어떤 질문이 반복되기 시작하면 `wiki/questions/`에 저장해야 하는가?
