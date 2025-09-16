# First_project

This repository contains examples of an "ESP" codex and utilities for generating or enhancing that codex.

## Codex generator

A simple Python script (`codex_generator.py`) reads a YAML or JSON fragment file and emits a full codex JSON file.  Use it to:

1. Maintain your codex entries in a human-editable `codex_input.yaml` (or your own file).
2. Run the generator:

```sh
python codex_generator.py codex_input.yaml -o codex.json
```

3. Inspect `codex.json` or feed it back to an LLM to expand or refactor the structure.

The input format is deliberately loose; anything under a top-level `codex:` key will be copied verbatim.

### Enhancing the codex with LLMs

To generate or extend entries automatically, you can provide your current codex as a prompt to a free LLM (e.g. ChatGPT free tier or a local GPT‑J model) and ask it to "add a new ring with these properties".  The output can then be merged back into `codex_input.yaml`.

## Other notes

The repository also contains a skill template (`SKILL.md`) for documenting workflows relevant to this project.
