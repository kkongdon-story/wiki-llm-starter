# LLM Wiki 운영 스킬 라우팅

이 문서는 `wiki-llm`을 실제 운영할 때 어떤 스킬을 언제 쓰는지 정리합니다.

## 1. 기본 원칙

초보자는 전역 스킬을 직접 고르지 않아도 됩니다. 먼저 repo-local 운영 스킬을 고르면 됩니다.

```text
wiki-ingest
wiki-query
wiki-lint
ontology-check
vibe-wiki-session
wiki-release
```

운영 스킬이 필요할 때만 전역 스킬을 연결합니다.

## 2. Repo-Local 운영 스킬

| 스킬 | 쓰는 순간 | 핵심 결과 |
| --- | --- | --- |
| `wiki-ingest` | raw 자료를 위키에 넣을 때 | source/concept/workflow page, ontology fact, log |
| `wiki-query` | 위키 기준으로 질문할 때 | 근거 있는 답변, 관련 wiki page, 저장할 질문 |
| `wiki-lint` | 위키 건강검진을 할 때 | 고립 문서, 출처 없는 주장, 모순 후보, 온톨로지 오류 |
| `ontology-check` | T-Box/A-Box/reasoner를 확인할 때 | domain/range 검사, inference 예시 |
| `vibe-wiki-session` | 바이브 코딩 작업을 시작할 때 | Query -> Plan -> Build -> Verify -> Ingest 루프 |
| `wiki-release` | ZIP/Git 배포 전 확인할 때 | 배포 패키지, 루트/패키지 검증 |

## 3. 전역 스킬 연결표

| 상황 | 먼저 쓰는 운영 스킬 | 필요한 전역 스킬 | 이유 |
| --- | --- | --- | --- |
| PDF를 raw로 넣고 싶다 | `wiki-ingest` | `pdf` | PDF 텍스트/구조 추출이 필요할 수 있음 |
| 음성/영상 자료를 넣고 싶다 | `wiki-ingest` | `transcribe` | 자막/텍스트화가 먼저 필요함 |
| 최신 정보인지 확인해야 한다 | `wiki-query` 또는 `wiki-ingest` | web search | 날짜, 버전, 가격, 법률, 뉴스는 바뀔 수 있음 |
| Obsidian graph나 로컬 화면을 확인해야 한다 | `wiki-lint` | `browser-use` 또는 `playwright` | 화면/브라우저 검증이 필요함 |
| OpenAI API 구현이 필요하다 | `vibe-wiki-session` | `openai-docs` | OpenAI 제품/SDK 사용법은 공식 문서 기준으로 확인해야 함 |
| 문서 산출물이 `.docx`다 | `vibe-wiki-session` | `documents` 또는 `docx` | 파일 형식별 생성/검증 필요 |
| 발표 자료가 필요하다 | `vibe-wiki-session` | `presentations` 또는 `pptx` | 슬라이드 생성/검증 필요 |
| 스프레드시트 산출물이 필요하다 | `vibe-wiki-session` | `spreadsheets` 또는 `xlsx` | 표/계산/시트 검증 필요 |
| 프론트엔드 앱을 만든다 | `vibe-wiki-session` | `frontend-design`, `browser-use`, `playwright` | UX 설계와 브라우저 검증 필요 |
| GitHub 배포/PR을 만든다 | `wiki-release` | `github` | 원격 저장소 작업이 필요할 때만 사용 |

## 4. 호출하지 말아야 할 경우

- 단순 Markdown source ingest에는 RAG/vector DB를 붙이지 않습니다.
- 이미 텍스트로 된 raw 자료에는 `pdf`나 `transcribe`를 부르지 않습니다.
- 단순 온톨로지 검사는 web search가 필요 없습니다.
- 이미지 생성을 원하지 않는데 `imagegen`을 쓰지 않습니다.
- 배포 ZIP만 만들 때는 GitHub 스킬을 쓰지 않습니다.

## 5. 초보자 명령 예시

```text
wiki-ingest로 raw 폴더에 있는 새 자료를 처리해줘.
```

```text
wiki-query로 내 위키 기준에서 이 질문에 답해줘: LLM Wiki와 RAG의 차이는 뭐야?
```

```text
ontology-check로 T-Box/A-Box와 domain/range 오류를 검사해줘.
```

```text
vibe-wiki-session으로 오늘 작업을 시작해줘. 먼저 기존 wiki를 읽고 성공 기준을 정한 다음 구현하고, 마지막에 배운 점을 wiki에 저장해줘.
```

```text
wiki-release로 초보자 배포용 ZIP을 만들고 패키지 안에서도 검증해줘.
```

## 6. 운영 흐름

평소에는 아래 순서만 기억하면 됩니다.

```text
자료가 생겼다 -> wiki-ingest
질문이 생겼다 -> wiki-query
상태가 의심된다 -> wiki-lint
관계가 맞는지 보고 싶다 -> ontology-check
작업을 시작한다 -> vibe-wiki-session
배포한다 -> wiki-release
```
