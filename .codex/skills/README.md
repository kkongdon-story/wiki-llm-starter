# Codex Skill Mirror

This folder mirrors `.agents/skills/` so Codex desktop/program surfaces that scan `.codex/skills` can show the repo-local Namba skills.

Canonical source:

```text
.agents/skills/
```

Visibility mirror:

```text
.codex/skills/
```

If `namba regen` refreshes `.agents/skills/`, rerun:

```text
& .\scripts\sync-codex-skills.ps1
```
