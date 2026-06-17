---
name: wiki-query
description: Answer questions from the compiled LLM Wiki before falling back to raw sources or web search.
---

# wiki-query

Use this skill when the user asks a question that should be answered from an LLM Wiki vault.

Korean triggers include:

- `wiki 기준으로 답해줘`
- `내 위키에서 찾아봐`
- `이 지식베이스 기준으로 질문에 답해줘`
- `raw를 처음부터 보지 말고 wiki에서 먼저 찾아줘`

## Goal

Answer from the compiled wiki layer first so knowledge compounds instead of restarting from raw sources every time.

## Inputs

- A wiki root. Default to `templates/llm-wiki` unless the user names another vault.
- User question.
- `wiki/index.md`.
- Related pages under `wiki/concepts`, `wiki/entities`, `wiki/workflows`, `wiki/questions`, and `wiki/sources`.

## Workflow

0. Run gbrain search to get relevant page paths (path hints only — do not use as the final answer):

```text
gbrain search "<question>"
```

Use the returned paths to prioritize which wiki pages to read first. Skip this step if gbrain is not installed.

1. Read `wiki/index.md`.
2. Identify the 3-7 most relevant wiki pages.
3. Read related concept/entity/workflow/question pages.
4. Use raw sources only when the wiki page points to them or when the answer requires source-level detail.
5. Answer with:
   - direct answer
   - supporting wiki pages
   - confidence and uncertainty
   - suggested next question
6. If the answer is reusable, ask whether to save it under `wiki/questions/` or save it directly when the user asked for durable update.

## Global Skill Routing

- Use web search when the user asks for current facts, recent news, current versions, current laws, prices, or time-sensitive information.
- Use `browser-use` or `playwright` when the answer depends on browser-visible behavior or Obsidian graph/UI verification.
- Use `openai-docs` when the question is specifically about OpenAI API, Agents SDK, ChatGPT Apps, or OpenAI product implementation.

## Output

Report:

- answer
- wiki pages used
- raw sources used, if any
- whether a new `wiki/questions/` page was created or recommended

