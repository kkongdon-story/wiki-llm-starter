---
name: wiki-lint
description: Health-check an LLM Wiki for broken structure, weak source grounding, stale claims, and ontology issues.
---

# wiki-lint

Use this skill when the user asks to lint, inspect, health-check, clean up, or audit the LLM Wiki.

Korean triggers include:

- `위키 상태 점검해줘`
- `LLM Wiki lint 해줘`
- `고립 문서와 출처 없는 주장 찾아줘`
- `온톨로지 오류까지 검사해줘`

## Goal

Keep the wiki useful as it grows. A wiki that only accumulates pages without linting becomes hard to trust.

## Checks

1. Folder contract:
   - `raw/`
   - `wiki/`
   - `schema/`
   - `ontology/`
2. Wiki structure:
   - orphan pages
   - missing backlinks
   - duplicated concepts
   - pages with no source signal
3. Claim quality:
   - source-less claims
   - contradiction candidates
   - stale claims
   - vague AI-generated wording
4. Ontology:
   - missing class
   - missing relation
   - missing domain/range
   - domain/range violation
   - disjoint-class conflict

## Workflow

1. Run:

```text
C:\Python313\python.exe scripts\lint_wiki.py --root <vault>
C:\Python313\python.exe scripts\ontology_reasoner.py --root <vault>
```

2. Inspect wiki pages when the script output is too shallow.
3. Separate findings into:
   - must fix now
   - should fix soon
   - optional cleanup
4. Do not delete pages unless the user explicitly asks or the acceptance criteria require cleanup.

## Global Skill Routing

- Use `browser-use` or `playwright` only when the user wants Obsidian graph or browser-visible verification.
- Do not use web search unless the lint issue depends on current external facts.

## Output

Report:

- command results
- lint findings
- ontology findings
- recommended fix order
- files changed, if fixes were requested

