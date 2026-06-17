---
name: wiki-ingest
description: Ingest raw sources into the LLM Wiki, update ontology facts, and run reasoner/lint checks.
---

# wiki-ingest

Use this skill when the user asks to ingest, absorb, process, or organize new material in an LLM Wiki vault.

Korean triggers include:

- `raw 자료 ingest 해줘`
- `이 자료를 위키에 넣어줘`
- `새 자료를 LLM Wiki에 흡수해줘`
- `원문을 읽고 wiki/ontology 업데이트해줘`

## Goal

Turn source material in `raw/` into durable wiki pages and ontology facts. This is not a one-shot summary.

## Inputs

- A wiki root. Default to `templates/llm-wiki` unless the user names another vault.
- Source files under `raw/`.
- Existing rules:
  - `CLAUDE.md`
  - `schema/wiki-rules.md`
  - `schema/page-template.md`
  - `ontology/tbox.json`
  - `ontology/abox.json`

## Workflow

1. Read the vault-level `CLAUDE.md` and schema files.
2. Identify unprocessed or newly named files in `raw/`.
3. For each source, extract:
   - source title
   - source type
   - key concepts
   - entities/tools/workflows
   - claims
   - uncertainty and missing metadata
4. Create or update `wiki/sources/<source-id>.md`.
5. Update related pages in:
   - `wiki/concepts/`
   - `wiki/entities/`
   - `wiki/workflows/`
6. Update `ontology/abox.json` with instances and facts that match `ontology/tbox.json`.
7. Append `log.md` with changed files and open questions.
8. Run:

```text
C:\Python313\python.exe scripts\ontology_reasoner.py --root <vault>
C:\Python313\python.exe scripts\lint_wiki.py --root <vault>
```

If `C:\Python313\python.exe` is not available, find the local Python executable and report the command used.

9. Only after steps 5–8 pass, sync updated wiki pages to gbrain:

```text
gbrain import wiki/
```

If gbrain is not installed, skip this step and note it in the report.

## Global Skill Routing

- Use `pdf` when the source is a PDF and text extraction or layout inspection is needed.
- Use `transcribe` when the source is audio/video and transcript extraction is needed.
- Use web search only when the user asks to refresh current facts or the source needs current verification.
- Do not use `imagegen` for source understanding. It generates/edits images and is not the right tool for reading image-based sources.

## Output

Report:

- raw files processed
- wiki pages created or updated
- ontology instances/facts added
- reasoner result
- lint result
- gbrain sync result (pages imported, or skipped if not installed)
- remaining uncertainties

