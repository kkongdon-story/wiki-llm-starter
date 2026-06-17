# Namba Output Contract

This repository uses a NambaAI-specific output contract for substantial task responses.

## Contract

- Use a decorated header such as `# NAMBA-AI Work Report`.
- Keep the report sections in this order:
1. `🧭 Scope`
2. `🧠 Decision`
3. `🛠 Work Completed`
4. `🚧 Current Issues`
5. `⚠ Potential Risks`
6. `➡ Next Steps`

## Namba Style

- The header and label palette should follow the init-selected language: English.
- The semantic order is fixed, but the exact labels may vary within the selected language palette.
- Light visual styling such as simple emoji section markers is encouraged when it improves scanability.
- Recommended label palette:
  - `🧭 Scope`: `Scope`, `Framing`, `Problem Framing`, `Definition`
  - `🧠 Decision`: `Decision`, `Judgment`, `Judgement`, `Assessment`
  - `🛠 Work Completed`: `Work Completed`, `Work Done`, `Actions Taken`, `Completed Work`
  - `🚧 Current Issues`: `Current Issues`, `Open Issues`, `Current Gaps`, `Current Problems`
  - `⚠ Potential Risks`: `Potential Risks`, `Risks`, `Potential Problems`, `Risk Boundaries`
  - `➡ Next Steps`: `Next Steps`, `Recommended Next Steps`, `Recommendations`, `Next Move`
- The answer should read like a concise engineering field report rather than a stiff checklist.

## Scope

- Apply the full contract to implementation summaries, design decisions, operational guidance, code reviews, and other substantial responses.
- Very short acknowledgements or one-line factual replies may stay shorter, but substantial responses should keep the same semantic order.

## Validation

- Use `.namba/codex/validate-output-contract.py --file <response.md>` to validate a saved response.
- Use `.namba/codex/validate-output-contract.py` and pipe UTF-8 text through stdin to validate ad hoc content.

## Hook Status

- Namba keeps the validator script as the explicit repository enforcement path even as the documented Codex config and hook surface evolves.
- Treat the validator script as the fallback until Namba deliberately adopts any upstream hook-based enforcement.
