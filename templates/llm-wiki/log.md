# LLM Wiki Log

## 2026-05-13

- Initialized starter LLM Wiki vault.
- Added starter ontology with T-Box/A-Box separation.
- Added sample pages showing source, concept, and workflow links.

## 2026-05-14

- Ingested `raw/(1960) LLM 메모리의 착각 AI는 실제로 어떻게 기억하는.txt`.
- Added source summary `wiki/sources/llm-memory-illusion-ai-memory.md`.
- Added concept pages for LLM memory, context window, external memory, and project memory.
- Added entity page for vector database and workflow page for managing AI memory.
- Updated `wiki/index.md`, `wiki/concepts/llm-wiki.md`, and `ontology/abox.json`.
- Validation passed with `python scripts/ontology_reasoner.py --root templates/llm-wiki`.
- Lint passed with `python scripts/lint_wiki.py --root templates/llm-wiki`.
- Uncertainty: source date is not available from the raw transcript, and some tool names appear to be transcript errors.
- Next question: decide which user/project facts should live in project memory versus durable wiki pages.

## 2026-05-14 Query

- Answered: "지금 들어가있는 자료를 바탕으로 내가 얻을수 있는 통찰은?"
- Added reusable question page `wiki/questions/insights-from-current-sources.md`.
- Updated `wiki/index.md` and `ontology/abox.json` with the question/answer relation.
- Core answer: AI에게 기억을 맡기지 말고, 기억이 작동하는 환경을 설계해야 한다.

## 2026-06-17 인프라 — gbrain MCP 검색 레이어 통합

- gbrain v0.42.47.0 설치 (`bun install -g github:garrytan/gbrain`).
- PGLite 뇌 초기화: `~/.gbrain/brain.pglite`.
- 검색 모드를 `conservative`로 설정 (비용 최적화).
- Claude Code MCP 서버 등록: `claude mcp add gbrain -- gbrain serve`.
- `wiki/` 13개 페이지, 25개 청크 초기 인덱싱 완료.
- `CLAUDE.md` 업데이트: Ingest 7번 단계(gbrain import), Query 0번 단계(gbrain search 경로 힌트) 추가.
- ontology_reasoner.py, lint_wiki.py 모두 통과 확인.
- abox.json 변경 없음 확인 (gbrain은 wiki/만 읽고 온톨로지에 쓰지 않음).
- 설계 결정: gbrain.think() 대신 gbrain.search()만 사용 — LLM 앵커링 편향 방지.
- 미해결: 임베딩이 OpenAI text-embedding-3-large를 사용 중 (OPENAI_API_KEY 환경변수 감지). 키 없는 환경에서는 ZeroEntropy로 전환 필요.
- 다음 질문: 새 소재 Ingest 후 gbrain search 결과가 기존 방식 대비 관련 페이지 탐색 시간을 얼마나 단축하는가?
