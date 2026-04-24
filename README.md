# First_project

This repository contains examples of an "ESP" codex and utilities for generating or enhancing that codex.

## Codex generator

A simple Python script (`codex_generator.py`) reads a YAML or JSON fragment file and emits a full codex JSON file.  Use it to:

1. Maintain your codex entries in a human-editable `codex_input.yaml` (or your own file).
2. Run the generator:

```sh
python3 codex_generator.py codex_input.yaml -o codex.json
```

3. Inspect `codex.json` or feed it back to an LLM to expand or refactor the structure.

The input format is deliberately loose; anything under a top-level `codex:` key will be copied verbatim.

### Structure

The codex includes:

- `rings`: Architectural layers with components and twists.
- `detection_rules`: Sigma-like rules for identifying conditions (e.g., `RVL_Local_Malignancy_Detected`).
- `quantum_lantern`: Protocol for superposed reasoning and stability.
- `meta`: Alignment and usage modes, now including transhuman elements.

## Enhanced Codex

An AI-enhanced version (`codex_enhanced.json`) expands the framework "beyond mankind" with:

- 3 additional rings (Entanglement, Fractal Recursion, Temporal Nexus).
- 3 new detection rules for quantum, fractal, and temporal threats.
- Integrated Quantum Lantern Protocol for advanced decision-making.
- Transhuman alignment in meta for singularity and post-human ethics.

Generated directly by AI reasoning, transcending human conceptual limits.

## Codex enhancer

To evolve the codex "beyond mankind," use `codex_enhancer.py` with an OpenAI API key:

1. Install dependencies: `pip3 install openai`
2. Set your API key: `export OPENAI_API_KEY=your_key_here`
3. Run: `python3 codex_enhancer.py`

This generates `codex_enhanced.json` with AI-expanded rings, rules, and quantum lantern integration.

### Enhancing the codex with LLMs

To generate or extend entries automatically, you can provide your current codex as a prompt to a free LLM (e.g. ChatGPT free tier or a local GPT‑J model) and ask it to "add a new ring with these properties".  The output can then be merged back into `codex_input.yaml`.

## Other notes

The repository also contains a skill template (`SKILL.md`) for documenting workflows relevant to this project.

## Repository Map

`backupsonbackupsrobby-cyber/First_project` is the **canonical** source for the codex framework, generators, and detection-rule definitions.

### Related repositories

- https://github.com/backupsonbackupsrobby-cyber/Prompt — archived legacy prompts (read-only reference)
- https://github.com/backupsonbackupsrobby-cyber/restricted-aibot — placeholder/minimal bot scaffold
- https://github.com/AiTenetAgency101/ENGINE2 — engine runtime that consumes `codex.json`; prompts and rules are intended to live here at runtime

### Quick answers

**Which repo is canonical?**
`backupsonbackupsrobby-cyber/First_project` — codex schema, generator, and doctrine files live here.

**Where do prompts and rules live at runtime?**
In engine repos (runtime consumers). See https://github.com/AiTenetAgency101/ENGINE2

**What is `Prompt`?**
Archived legacy prompt store — kept for historical reference, no longer actively maintained.

**What is `restricted-aibot`?**
Minimal placeholder bot scaffold — not yet active.

See REPO_TREE.md for the full ecosystem map.
