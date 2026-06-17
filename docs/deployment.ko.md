# 배포 가이드

이 프로젝트는 개발자와 비개발자 모두 사용할 수 있게 Git 다운로드와 ZIP 다운로드를 기준으로 설계합니다.

## Git으로 받기

```text
git clone <repo-url>
cd wiki-llm
```

## ZIP으로 받기

1. GitHub 저장소에서 `Code`를 누릅니다.
2. `Download ZIP`을 누릅니다.
3. 압축을 풉니다.
4. 압축을 푼 폴더 안에서 `templates/llm-wiki` 폴더를 복사해서 내 프로젝트 이름으로 바꿉니다.
5. Obsidian에서 복사한 폴더를 vault로 엽니다.

`scripts/` 폴더는 검사 도구입니다. 템플릿 vault만 다른 곳으로 옮길 때도 `scripts/` 위치를 함께 관리해야 합니다.

## 배포에 포함해야 할 것

- `START_HERE.ko.md`
- `docs/user-manual.ko.md`
- `docs/llm-wiki-rules.ko.md`
- `docs/ontology-guide.ko.md`
- `templates/llm-wiki/`
- `.agents/skills/`
- `.codex/skills/`
- `scripts/ontology_reasoner.py`
- `scripts/lint_wiki.py`

## 배포 전에 확인할 것

```text
python scripts/ontology_reasoner.py --root templates/llm-wiki
python scripts/lint_wiki.py --root templates/llm-wiki
```

두 명령이 통과하면 최소 배포 가능한 상태입니다.

운영 스킬까지 포함한 배포 패키지는 `scripts/package_release.ps1`로 만듭니다. 이 패키지에는 사용자가 명령처럼 부를 수 있는 `wiki-ingest`, `wiki-query`, `wiki-lint`, `ontology-check`, `vibe-wiki-session`, `wiki-release` 스킬이 함께 들어갑니다.
