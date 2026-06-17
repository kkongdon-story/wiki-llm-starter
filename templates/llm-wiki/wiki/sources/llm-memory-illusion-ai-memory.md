# LLM Memory Illusion: How AI Actually Remembers

type: source
source_id: llm_memory_illusion_ai_memory
raw: raw/(1960) LLM 메모리의 착각 AI는 실제로 어떻게 기억하는.txt

## One-line Definition

이 유튜브 자막 자료는 LLM의 "기억"이 실제 장기 기억이라기보다 컨텍스트 윈도우, 요약, 외부 메모리 주입으로 만들어지는 작동 효과라고 설명한다.

## Summary

자료의 핵심 주장은 LLM이 기본적으로 이전 대화를 생물학적 기억처럼 저장하지 않는다는 것이다. 사용자가 메시지를 보낼 때 시스템은 현재 메시지만 보내는 것이 아니라, 가능한 범위 안에서 이전 대화 기록을 함께 붙여 LLM에게 다시 읽힌다.

이때 모델이 볼 수 있는 텍스트 묶음이 [[concepts/context-window]]이며, 자료는 이를 단기 기억에 비유한다. 컨텍스트 한계를 넘으면 오래된 대화는 삭제되거나 요약되거나, 별도 저장소에서 관련 사실만 다시 불러오는 방식이 사용된다.

자료는 네 가지 관리 전략을 구분한다.

- 전체 대화 기록을 계속 넣는 방식
- 최근 메시지만 유지하는 슬라이딩 윈도우
- 오래된 대화를 압축하는 요약
- 벡터 DB 같은 외부 저장소에서 관련 사실을 다시 주입하는 [[concepts/external-memory]]

마지막으로 사용자는 대화 기록과 memory facts를 구분해야 하며, 장기적으로 AI가 무엇을 기억하게 할지 의도적으로 관리해야 한다고 강조한다.

## Source Links

- Raw source: `raw/(1960) LLM 메모리의 착각 AI는 실제로 어떻게 기억하는.txt`
- YouTube URL in raw source: `https://www.youtube.com/watch?v=HW1a5l1M6Bw`

## Related Pages

- [[concepts/llm-memory]]
- [[concepts/context-window]]
- [[concepts/external-memory]]
- [[concepts/project-memory]]
- [[entities/vector-database]]
- [[workflows/manage-ai-memory]]
- [[concepts/llm-wiki]]

## Extracted Claims

- LLM은 기본적으로 세션을 넘어서는 기억을 갖지 않으며, 현재 프롬프트에 포함된 정보만 볼 수 있다.
- 대화가 이어지는 것처럼 보이는 이유는 시스템이 이전 메시지들을 현재 요청에 다시 붙여 보내기 때문이다.
- [[concepts/context-window]]는 LLM의 단기 기억처럼 작동하지만, 토큰 한계가 있어 오래된 정보가 밀려날 수 있다.
- [[concepts/external-memory]]는 대화 밖에 저장된 사실을 필요할 때 프롬프트에 다시 주입하는 방식이다.
- 사용자는 대화 기록과 memory facts를 구분하고, 장기 기억에 남길 정보를 의도적으로 관리해야 한다.

## Reliability Limits

- 이 자료는 유튜브 설명 자막이며, 원문 발표일과 세부 출처는 raw 파일만으로 확인되지 않는다.
- 도구 이름 일부는 자막 변환 과정에서 잘못 적혔을 가능성이 있다. 예: `claw.ai`, `clot code`, `Claude Senate`.
- 모델별 컨텍스트 길이와 제품별 메모리 기능은 시간이 지나며 바뀔 수 있으므로, 현재 스펙으로 쓰려면 별도 최신 확인이 필요하다.

## Open Questions

- 이 위키에서는 어떤 정보를 장기 memory facts로 저장하고, 어떤 정보는 source summary에만 남겨야 하는가?
- 프로젝트별 permanent memory 파일은 어디까지 원칙화해야 하는가?
