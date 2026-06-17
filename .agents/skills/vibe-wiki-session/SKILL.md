---
name: vibe-wiki-session
description: Run a vibe-coding work session with LLM Wiki memory before and after the build loop.
---

# vibe-wiki-session

Use this skill when the user wants to connect vibe coding with the LLM Wiki system.

Korean triggers include:

- `바이브 코딩 세션 시작하자`
- `wiki 기반으로 오늘 작업 시작해줘`
- `작업 전 지식 불러오고 끝나면 위키에 저장해줘`
- `Query Plan Build Verify Ingest 루프로 해줘`

## Goal

Prevent vibe coding from becoming disposable one-off work. Each session should start from the wiki and end by updating the wiki.

## Loop

```text
Query -> Plan -> Build -> Verify -> Ingest -> Evolve
```

## Workflow

### 1. Query

Run gbrain search to get relevant page paths first (skip if gbrain not installed):

```text
gbrain search "<today's task or question>"
```

Then read `wiki/index.md` and the returned pages. Summarize:

- existing decisions
- existing constraints
- previous failures
- relevant workflows

### 2. Plan

Write a short success criterion:

- what should work
- what should not change
- how to verify it

### 3. Build

Make the requested change. Keep edits scoped.

### 4. Verify

Run relevant commands:

- reasoner
- lint
- tests
- browser checks, if needed

### 5. Ingest

Update wiki pages and `log.md` with:

- decision made
- files changed
- reusable prompt or procedure
- open questions

Then sync to gbrain (skip if not installed):

```text
gbrain import wiki/
```

### 6. Evolve

If a pattern repeats:

- promote repeated instructions to `schema/`
- promote repeated relationships to `ontology/`
- keep one-off observations as normal wiki notes

## Global Skill Routing

- Use `browser-use` or `playwright` for browser-rendered verification.
- Use `documents`, `presentations`, or `spreadsheets` for `.docx`, `.pptx`, or spreadsheet deliverables.
- Use `openai-docs` for OpenAI API or Agents SDK implementation.
- Use `frontend-design` only when the session includes actual frontend UX work.

## Output

Report in this order:

1. existing wiki context used
2. success criteria
3. changes made
4. verification results
5. wiki/ontology updates
6. next best action

