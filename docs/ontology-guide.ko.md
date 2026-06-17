# Ontology LLM Wiki 가이드

이 문서는 단순 LLM Wiki를 온톨로지 기반 지식 시스템으로 확장하는 방법을 설명합니다.

## 1. 온톨로지가 필요한 이유

위키는 사람이 읽기 좋습니다. 하지만 위키만 있으면 AI가 관계를 느슨하게 해석할 수 있습니다.

온톨로지는 다음을 강제합니다.

- 어떤 종류의 개념이 있는가
- 어떤 관계가 허용되는가
- 관계의 주어와 목적어는 어떤 종류여야 하는가
- 어떤 사실이 서로 충돌하는가
- 어떤 사실을 새로 추론할 수 있는가

## 2. T-Box와 A-Box

### T-Box

T-Box는 개념 체계입니다. "세상에 어떤 종류가 있는가"를 정의합니다.

예:

- `Source`
- `WikiPage`
- `Concept`
- `Tool`
- `Workflow`
- `Claim`

그리고 관계도 T-Box에 들어갑니다.

예:

- `derived_from`: `WikiPage -> Source`
- `mentions`: `SourceOrPage -> Concept`
- `uses_tool`: `Workflow -> Tool`

### A-Box

A-Box는 실제 사례입니다. "내 지식 시스템에 실제로 무엇이 있는가"를 정의합니다.

예:

- `karpathy_llm_wiki_post`는 `Source`
- `llm_wiki`는 `Concept`
- `obsidian`은 `Tool`
- `ingest_workflow`는 `Workflow`
- `ingest_workflow uses_tool obsidian`

## 3. domain과 range

모든 관계에는 domain과 range가 있어야 합니다.

예:

```json
{
  "id": "derived_from",
  "label": "출처에서 파생됨",
  "domain": "WikiPage",
  "range": "Source"
}
```

이 뜻은 다음과 같습니다.

- `derived_from`의 주어는 `WikiPage`여야 합니다.
- `derived_from`의 목적어는 `Source`여야 합니다.

만약 `Concept derived_from Source`라고 쓰면 reasoner가 오류를 잡아야 합니다.

## 4. Reasoner가 하는 일

이 저장소의 starter reasoner는 `scripts/ontology_reasoner.py`입니다.

검사하는 것:

- T-Box에 없는 class를 instance가 쓰는지
- T-Box에 없는 relation을 fact가 쓰는지
- relation의 domain/range가 맞는지
- 서로 disjoint인 class를 동시에 갖는 instance가 있는지

추론하는 것:

- 하위 class면 상위 class 타입도 추론합니다.
- relation의 domain/range를 보고 빠진 타입을 추론합니다.
- inverse relation을 자동 생성합니다.
- `inference-rules.json`에 적은 간단한 규칙을 적용합니다.

## 5. Inference 예시

`wiki_llm_rules_page derived_from karpathy_llm_wiki_post`라는 fact가 있고, `derived_from`의 domain/range가 `WikiPage -> Source`라면 reasoner는 다음을 확인하거나 추론합니다.

- `wiki_llm_rules_page`는 `WikiPage`여야 한다.
- `karpathy_llm_wiki_post`는 `Source`여야 한다.

또 `karpathy_llm_wiki_post mentions llm_wiki`가 있고, 규칙에 아래처럼 적혀 있다면:

```text
page derived_from source
source mentions concept
=> page mentions concept
```

reasoner는 다음을 추론합니다.

```text
wiki_llm_rules_page mentions llm_wiki
```

이 추론 덕분에 위키 페이지와 원문 사이의 개념 연결이 자동으로 늘어납니다.

## 6. 초보자에게 설명하는 방식

너무 어렵게 말하지 않아도 됩니다.

- T-Box: 분류표
- A-Box: 실제 카드 목록
- relation: 카드끼리 연결하는 선
- domain/range: 이 선을 어떤 카드 사이에만 그을 수 있는지 정한 규칙
- reasoner: 잘못 그은 선과 자동으로 그릴 수 있는 선을 찾아주는 검사기

## 7. 확장 순서

처음부터 큰 온톨로지를 만들지 마세요.

1. `Source`, `Concept`, `WikiPage`, `Tool`, `Workflow`, `Claim`만 둡니다.
2. 자료 5개를 ingest 합니다.
3. 반복되는 관계만 formal relation으로 올립니다.
4. domain/range를 추가합니다.
5. reasoner 오류가 계속 0이 되는지 봅니다.
6. 그 다음 세부 class를 나눕니다.
