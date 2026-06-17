# LLM Wiki Ontology Starter

이 프로젝트는 Andrej Karpathy가 말한 LLM Wiki 방식을 초보자도 쓸 수 있게 만든 시작 템플릿입니다.

목표는 단순히 자료를 검색하는 RAG가 아닙니다. 자료를 한 번 읽고, AI가 내 지식 체계에 흡수해서, 시간이 지날수록 더 잘 정리되는 개인/업무용 지식 시스템을 만드는 것입니다.

## 1분 요약

- `raw/`: 원본 자료를 넣는 곳입니다. 기사, 회의록, 유튜브 자막, PDF에서 뽑은 텍스트, 내 메모가 들어갑니다.
- `wiki/`: AI가 만든 지식 페이지가 들어가는 곳입니다. 사람은 주로 읽고 검토합니다.
- `schema/`: AI에게 "어떤 방식으로 정리할지" 알려주는 규칙입니다.
- `ontology/`: 개념 체계입니다. 개념 종류, 관계, 실제 사례, 추론 규칙을 분리합니다.
- `scripts/`: 위키와 온톨로지를 검사하는 도구입니다.

## 가장 먼저 할 일

1. ZIP 또는 Git으로 받은 패키지 루트는 그대로 둡니다. `scripts/`가 검사 도구이므로 함께 있어야 합니다.
2. `templates/llm-wiki` 폴더를 같은 패키지 안에서 복사해서 내 지식 주제 이름으로 바꿉니다.
   - 예: `my-life-wiki`, `sales-wiki`, `study-wiki`
3. Obsidian에서 그 폴더를 vault로 엽니다.
4. `raw/`에 첫 자료 하나를 넣습니다.
5. (권장) gbrain 검색 레이어를 설치합니다. 한 번만 하면 됩니다.

```text
bun install -g github:garrytan/gbrain
gbrain init --pglite
claude mcp add gbrain -- gbrain serve
gbrain import templates/llm-wiki/wiki/
```

6. Claude Code, Codex, Cursor 같은 에이전트에게 아래처럼 말합니다.

```text
templates/llm-wiki/CLAUDE.md 규칙을 읽고 raw/ 안의 자료를 ingest 해줘.
wiki/ 페이지, ontology/abox.json, log.md를 함께 업데이트하고,
마지막에 scripts/ontology_reasoner.py로 온톨로지 검사를 실행해줘.
검사가 통과하면 gbrain import wiki/ 로 검색 인덱스도 업데이트해줘.
```

## 왜 RAG만으로 끝내지 않나

RAG는 질문할 때마다 원문 조각을 다시 찾습니다. 답변은 유용하지만, 그 답변이 지식 구조 안에 누적되지 않습니다.

LLM Wiki는 반대로 작동합니다. 원문을 읽은 뒤 AI가 위키 페이지, 개념 관계, 출처, 충돌 가능성을 계속 업데이트합니다. 그래서 두 번째 질문은 첫 번째 질문보다 더 나은 상태에서 시작합니다.

## 이 템플릿의 추가 목표

이 저장소는 기본 LLM Wiki 위에 온톨로지 레이어를 둡니다.

- 도메인의 개념 체계를 `ontology/tbox.json`에 정의합니다.
- 실제 사례와 자료는 `ontology/abox.json`에 둡니다.
- 관계마다 `domain`과 `range`를 둡니다.
- `scripts/ontology_reasoner.py`로 일관성과 추론 결과를 확인합니다.
- 추론 결과를 사람이 이해할 수 있게 설명합니다.

## 초보자용 운영 순서

1. 자료를 넣습니다.
2. AI에게 ingest를 시킵니다.
3. AI가 wiki와 ontology를 업데이트합니다.
4. 검사 스크립트를 실행합니다.
5. 틀린 관계나 모순이 있으면 AI에게 고치라고 합니다.
6. gbrain이 자동으로 검색 인덱스를 업데이트합니다.
7. 좋은 질문/답변은 다시 wiki에 저장합니다.

## 배포 방식

이 프로젝트는 GitHub에서 clone해서 써도 되고, ZIP으로 내려받아도 됩니다.

- Git 사용자: `git clone <repo-url>`
- 비개발자: GitHub의 `Code -> Download ZIP`
- 시작 폴더: `templates/llm-wiki`
- 주의: `templates/llm-wiki`만 다른 곳으로 옮기면 검사 스크립트가 끊길 수 있습니다. 옮길 때는 `scripts/`도 함께 보관하세요.

다른 사용자에게 전달할 수 있는 전체 사용 설명서는 [docs/user-manual.ko.md](docs/user-manual.ko.md)를 보세요.

자세한 설계는 [docs/llm-wiki-rules.ko.md](docs/llm-wiki-rules.ko.md)와 [docs/ontology-guide.ko.md](docs/ontology-guide.ko.md)를 보세요.

내 삶에 어떻게 적용할지 막막하면 [docs/life-application-guide.ko.md](docs/life-application-guide.ko.md)를 먼저 보세요.

바이브 코딩과 연결해서 계속 발전시키는 운영 전략은 [docs/vibe-coding-operation-strategy.ko.md](docs/vibe-coding-operation-strategy.ko.md)를 보세요.

## 명령처럼 쓰는 운영 스킬

이 프로젝트를 실제로 굴릴 때는 아래 스킬 이름을 그대로 말하면 됩니다.

```text
wiki-ingest로 raw 자료를 넣어줘.
```

```text
wiki-query로 내 위키 기준에서 질문에 답해줘.
```

```text
wiki-lint로 위키 건강검진을 해줘.
```

```text
ontology-check로 T-Box/A-Box와 domain/range 오류를 검사해줘.
```

```text
vibe-wiki-session으로 오늘 작업을 시작해줘.
```

```text
wiki-release로 배포 ZIP을 만들고 검증해줘.
```

어떤 스킬이 어떤 전역 스킬과 연결되는지는 [docs/skill-routing.ko.md](docs/skill-routing.ko.md)를 보세요.
