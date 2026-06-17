# LLM Wiki 구조화 규칙

이 문서는 Karpathy식 LLM Wiki를 실제로 운영하기 위한 규칙입니다.

## 1. 기본 판단

LLM Wiki는 검색 도구가 아니라 누적 지식 시스템입니다.

| 방식 | 작동 방식 | 장점 | 한계 |
| --- | --- | --- | --- |
| 일반 채팅 | 매번 자료를 붙이고 질문 | 빠름 | 대화가 끝나면 지식이 사라짐 |
| RAG | 질문할 때 관련 조각 검색 | 대량 문서 검색에 강함 | 구조와 관계가 누적되지 않음 |
| LLM Wiki | AI가 원문을 위키로 컴파일 | 지식과 관계가 축적됨 | 규칙과 검사가 없으면 품질이 흔들림 |
| Ontology LLM Wiki | 위키 + 개념 체계 + 추론 검사 | 확장성과 일관성 확보 | 초기에 작은 설계가 필요 |

## 2. 권장 폴더 구조

```text
my-wiki/
  CLAUDE.md
  log.md
  raw/
  wiki/
    index.md
    sources/
    concepts/
    entities/
    workflows/
    questions/
  schema/
    wiki-rules.md
    page-template.md
  ontology/
    tbox.json
    abox.json
    inference-rules.json
```

## 3. 세 레이어

### Raw Sources

원본 자료입니다. 원칙적으로 수정하지 않습니다.

예:

- 기사
- 유튜브 자막
- 회의록
- 강의 노트
- PDF에서 추출한 텍스트
- 내 경험 메모

### Wiki

AI가 관리하는 지식 페이지입니다.

좋은 wiki 페이지는 다음을 가집니다.

- 한 문장 정의
- 핵심 요약
- 관련 개념 링크
- 출처 링크
- 확실한 것과 불확실한 것
- 다음 질문

### Schema

AI가 문서를 어떻게 다뤄야 하는지 정한 규칙입니다.

Schema가 없으면 AI는 매번 다른 방식으로 정리합니다. Schema가 있으면 같은 방식으로 계속 누적됩니다.

## 4. 세 작업

### ingest

새 자료를 지식 체계에 넣는 작업입니다.

성공 기준:

- 원문 출처가 남아 있다.
- source summary가 생겼다.
- 관련 concept/entity/workflow 페이지가 업데이트됐다.
- ontology A-Box에 실제 instance/fact가 추가됐다.
- reasoner 검사 결과가 통과했다.
- log에 변경 사항이 남았다.

### query

질문에 답하는 작업입니다.

성공 기준:

- raw를 매번 처음부터 읽지 않고 index/wiki/ontology를 먼저 본다.
- 답변에 근거 페이지가 있다.
- 답변 중 재사용 가치가 높은 내용은 wiki에 저장한다.
- 모르는 부분은 모른다고 표시한다.

### lint

지식 체계 건강검진입니다.

성공 기준:

- 고립 문서를 찾는다.
- 출처 없는 주장을 찾는다.
- 모순되는 주장을 찾는다.
- 오래된 정보를 찾는다.
- ontology의 domain/range 위반을 찾는다.

## 5. 좋은 규칙의 기준

이 프로젝트에서는 여러 LLM Wiki 의견 중 아래 기준에 맞는 구조를 채택합니다.

1. 초보자가 폴더만 보고 이해할 수 있어야 한다.
2. Obsidian에서 바로 볼 수 있어야 한다.
3. Git 또는 ZIP으로 배포 가능해야 한다.
4. AI가 파일을 읽고 쓸 수 있어야 한다.
5. raw 원본과 AI 생성물을 분리해야 한다.
6. 위키가 커져도 lint와 ontology로 품질을 점검할 수 있어야 한다.
7. 처음부터 복잡한 DB나 서버를 요구하지 않아야 한다.

## 6. 언제 RAG를 추가하나

처음에는 Markdown Wiki로 시작합니다.

RAG나 vector DB는 아래 상황에서만 추가합니다.

- 문서가 수천 개 이상이다.
- wiki index만으로 관련 페이지를 찾기 어렵다.
- 검색 속도가 실제 병목이다.
- 팀 단위 접근 권한 관리가 필요하다.

즉, RAG는 LLM Wiki를 대체하는 것이 아니라 커졌을 때 붙이는 검색 보조 레이어입니다.
