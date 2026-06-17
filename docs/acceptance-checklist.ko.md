# 수용 기준 체크리스트

이 문서는 프로젝트 목표가 실제 산출물로 연결됐는지 확인하기 위한 체크리스트입니다.

## 1. Karpathy식 LLM Wiki 구조화 규칙

- [x] `raw / wiki / schema` 구조가 있다.
  - 증거: `templates/llm-wiki/raw`, `templates/llm-wiki/wiki`, `templates/llm-wiki/schema`
- [x] `ingest / query / lint` 운영 규칙이 있다.
  - 증거: `CLAUDE.md`, `templates/llm-wiki/CLAUDE.md`, `docs/llm-wiki-rules.ko.md`
- [x] RAG와 LLM Wiki의 차이를 설명한다.
  - 증거: `docs/llm-wiki-rules.ko.md`

## 2. 온톨로지 확장성

- [x] 도메인의 개념 체계를 정의했다.
  - 증거: `templates/llm-wiki/ontology/tbox.json`
- [x] T-Box와 A-Box를 분리했다.
  - 증거: `ontology/tbox.json`, `ontology/abox.json`
- [x] 관계마다 domain과 range를 정의했다.
  - 증거: `ontology/tbox.json`의 `relations`
- [x] Reasoner로 추론 검사를 할 수 있다.
  - 증거: `scripts/ontology_reasoner.py`
- [x] Inference 예시를 설명할 수 있다.
  - 증거: `docs/ontology-guide.ko.md`, `ontology/inference-rules.json`

## 3. 초보자 적용 가능성

- [x] 처음 보는 사람이 시작할 문서가 있다.
  - 증거: `START_HERE.ko.md`
- [x] 다른 사용자가 설치, 운영, 검증, 배포를 따라갈 수 있는 기술 사용 설명서가 있다.
  - 증거: `docs/user-manual.ko.md`
- [x] 삶/업무/공부에 적용하는 예시가 있다.
  - 증거: `docs/life-application-guide.ko.md`
- [x] 어려운 개념을 쉬운 말로 바꿔 설명한다.
  - 증거: `docs/ontology-guide.ko.md`

## 4. 배포 가능성

- [x] Git clone으로 받을 수 있는 일반 파일 구조다.
- [x] ZIP 다운로드 후 바로 복사해서 쓸 템플릿 폴더가 있다.
  - 증거: `templates/llm-wiki`
- [x] 로컬 ZIP 패키징 스크립트가 있다.
  - 증거: `scripts/package_release.ps1`
- [x] 배포 전 검증 명령이 있다.
  - 증거: `docs/deployment.ko.md`

## 5. 현재 검증 명령

```text
python scripts/ontology_reasoner.py --root templates/llm-wiki
python scripts/lint_wiki.py --root templates/llm-wiki
```

두 명령이 모두 통과해야 최소 배포 가능한 상태로 본다.

## 6. 바이브 코딩 운영 전략

- [x] 바이브 코딩과 LLM Wiki의 역할 분리를 설명한다.
  - 증거: `docs/vibe-coding-operation-strategy.ko.md`
- [x] 작업 전 query, 작업 중 build, 작업 후 ingest 루프를 정의한다.
  - 증거: `docs/vibe-coding-operation-strategy.ko.md`
- [x] 초보자용 하루 운영법을 포함한다.
  - 증거: `docs/vibe-coding-operation-strategy.ko.md`
- [x] 지속 디벨롭 전략과 과복잡화 방지 기준을 포함한다.
  - 증거: `docs/vibe-coding-operation-strategy.ko.md`

## 7. 실제 운영 스킬 패키지

- [x] raw ingest 운영 스킬이 있다.
  - 증거: `.agents/skills/wiki-ingest/SKILL.md`
- [x] wiki query 운영 스킬이 있다.
  - 증거: `.agents/skills/wiki-query/SKILL.md`
- [x] wiki lint 운영 스킬이 있다.
  - 증거: `.agents/skills/wiki-lint/SKILL.md`
- [x] ontology check 운영 스킬이 있다.
  - 증거: `.agents/skills/ontology-check/SKILL.md`
- [x] vibe coding session 운영 스킬이 있다.
  - 증거: `.agents/skills/vibe-wiki-session/SKILL.md`
- [x] release packaging 운영 스킬이 있다.
  - 증거: `.agents/skills/wiki-release/SKILL.md`
- [x] 전역 스킬 라우팅 문서가 있다.
  - 증거: `docs/skill-routing.ko.md`
- [x] 배포 ZIP에 운영 스킬 표면이 포함된다.
  - 증거: `scripts/package_release.ps1`가 `.agents/skills`와 `.codex/skills`를 포함
