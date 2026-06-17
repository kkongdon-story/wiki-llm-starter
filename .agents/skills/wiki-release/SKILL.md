---
name: wiki-release
description: Package and verify the LLM Wiki starter as a Git/ZIP-distributable beginner template.
---

# wiki-release

Use this skill when the user asks to create, verify, package, ship, or distribute the LLM Wiki starter.

Korean triggers include:

- `배포 ZIP 만들어줘`
- `릴리즈 패키지 검증해줘`
- `초보자에게 배포 가능한 상태로 만들어줘`
- `Git/ZIP 다운로드 구조 확인해줘`

## Goal

Produce a beginner-safe distributable package that contains the starter docs, scripts, and `templates/llm-wiki` vault.

## Workflow

1. Run root validation:

```text
C:\Python313\python.exe scripts\ontology_reasoner.py --root templates\llm-wiki
C:\Python313\python.exe scripts\lint_wiki.py --root templates\llm-wiki
```

2. Run packaging:

```text
& .\scripts\package_release.ps1
```

3. Verify files:

- `dist/wiki-llm-starter.zip`
- `dist/wiki-llm-starter/START_HERE.ko.md`
- `dist/wiki-llm-starter/docs/skill-routing.ko.md`
- `dist/wiki-llm-starter/templates/llm-wiki/CLAUDE.md`

4. Run validation inside package:

```text
C:\Python313\python.exe scripts\ontology_reasoner.py --root templates\llm-wiki
C:\Python313\python.exe scripts\lint_wiki.py --root templates\llm-wiki
```

from `dist/wiki-llm-starter`.

## Global Skill Routing

- Use `github` only if the user asks to publish or prepare a GitHub PR/release.
- Do not use presentation/document/spreadsheet skills unless the release includes those file formats.

## Output

Report:

- package path
- package size
- included docs
- root validation result
- package validation result
- remaining release risks

