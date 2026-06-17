<div align="center">

<h1>🧠 LLM Wiki Starter</h1>

<p><strong>자료를 넣을수록 더 똑똑해지는 AI 지식 뇌</strong></p>

<p>AI가 내 맥락을 기억하고, 자료가 쌓일수록 더 정확하게 답하는 지식의 복리 시스템</p>

<p>
  <img src="https://img.shields.io/badge/Claude_Code-지원-7c6af7?style=flat-square" />
  <img src="https://img.shields.io/badge/Codex-지원-34c759?style=flat-square" />
  <img src="https://img.shields.io/badge/gbrain-검색_레이어-ff9f0a?style=flat-square" />
  <img src="https://img.shields.io/badge/초보자-친화적-0a84ff?style=flat-square" />
</p>

<p>
  <a href="https://kkongdon-story.github.io/wiki-llm-starter/user-guide.html"><strong>📖 완전 사용 설명서</strong></a> &nbsp;|&nbsp;
  <a href="START_HERE.ko.md"><strong>🚀 빠른 시작</strong></a>
</p>

</div>

---

## 무엇이 다른가요?

| 기존 방식 (RAG) | 이 시스템 |
|---|---|
| 매번 맥락을 새로 설명 | wiki/에 누적되어 영구 보존 |
| 자료가 흩어져 연결 안 됨 | 개념 간 연결이 자동 형성 |
| 좋은 답변이 다음 대화에서 사라짐 | 답변이 다음 질문의 출발점이 됨 |
| 두 번째 질문이 첫 번째보다 나아지지 않음 | 자료가 쌓일수록 AI가 더 정확하게 답함 |

## 자료가 답변이 되는 흐름

```
📄 원본 자료  →  🤖 AI 분석  →  📚 지식 페이지  →  ✅ 구조 검증  →  🔍 검색 인덱스  →  💡 정확한 답변
   raw/           wiki-ingest      wiki/              ontology          gbrain              wiki-query
```

## 빠른 시작

```bash
# 1. gbrain 설치 (한 번만)
bun install -g github:garrytan/gbrain
gbrain init --pglite

# 2. Claude Code에 연결
claude mcp add gbrain -- gbrain serve

# 3. wiki 인덱싱
gbrain import templates/llm-wiki/wiki/
```

그 다음 Claude Code에서:

```
wiki-ingest로 raw 안의 자료를 넣어줘
```

> **터미널이 낯선 분** → [`docs/user-guide.html`](docs/user-guide.html)의 🚀 첫 걸음 탭에서 ZIP 해제부터 첫 사용까지 시각적으로 안내합니다.

## 운영 스킬

| 스킬 | Claude Code | Codex | 역할 |
|---|---|---|---|
| `wiki-ingest` | `wiki-ingest로 raw 자료 넣어줘` | `$wiki-ingest` | raw/ → wiki + ontology + gbrain |
| `wiki-query` | `wiki-query로 [질문] 답해줘` | `$wiki-query` | wiki 기반 질문 답변 |
| `wiki-lint` | `wiki-lint로 건강검진 해줘` | `$wiki-lint` | 링크·출처·고아 페이지 검사 |
| `ontology-check` | `ontology-check로 구조 검사해줘` | `$ontology-check` | T-Box/A-Box 일관성 검증 |
| `vibe-wiki-session` | `vibe-wiki-session으로 시작해줘` | `$vibe-wiki-session` | 세션 시작 맥락 불러오기 + 종료 저장 |

## 폴더 구조

```
wiki-llm-starter/
├── templates/llm-wiki/     ← 시작 템플릿 (여기를 복사해서 씀)
│   ├── raw/                ← 원본 자료 넣는 곳 (수정 금지)
│   ├── wiki/               ← AI가 정리한 지식 페이지
│   ├── ontology/           ← 개념 체계 (tbox.json / abox.json)
│   └── schema/             ← 페이지 작성 규칙
├── scripts/                ← 온톨로지·링크 검사 도구
├── docs/                   ← 사용 설명서
│   └── user-guide.html     ← 9탭 완전 가이드 (여기부터 읽으세요)
└── CLAUDE.md               ← AI 행동 규칙
```

## 문서

| 문서 | 내용 |
|---|---|
| [📖 완전 사용 설명서](https://kkongdon-story.github.io/wiki-llm-starter/user-guide.html) | ZIP 해제부터 고급 사용까지 9개 탭 HTML 가이드 |
| [🚀 빠른 시작](START_HERE.ko.md) | 1분 요약 + 첫 ingest 실행 |
| [📐 운영 규칙](docs/llm-wiki-rules.ko.md) | Ingest / Query / Lint 상세 절차 |
| [🗺️ 온톨로지 가이드](docs/ontology-guide.ko.md) | T-Box / A-Box 설계 원칙 |
| [💡 실생활 적용](docs/life-application-guide.ko.md) | 내 삶에 어떻게 적용할지 막막할 때 |
| [🛠️ 바이브 코딩 전략](docs/vibe-coding-operation-strategy.ko.md) | AI와 함께 프로덕트를 만드는 운영법 |

---

<div align="center">
  <sub>Andrej Karpathy의 LLM Wiki 방식을 초보자도 쓸 수 있게 만든 시작 템플릿</sub>
</div>
