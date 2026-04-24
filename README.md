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

---

## Repository Map

This section answers: **"Which repo is canonical?"** and **"Where do prompts live?"**

**This repo (`First_project`) is the canonical entry point** for the ESP codex framework, generators, and detection rules.

### Related Repositories

- **backupsonbackupsrobby-cyber/vs-studioPROMPT** (private, active)
  VS Code prompt and rule authoring workspace. This is where rule drafts and spec files like `RVL_Local_Malignancy_Detected` are written. Not public.
  https://github.com/backupsonbackupsrobby-cyber/vs-studioPROMPT

- **backupsonbackupsrobby-cyber/Prompt** (public, archived — legacy only)
  Legacy snippet scratchpad. Contains early concept fragments. This repo is archived and read-only; it is not canonical. For active codex work, use this repo (`First_project`) instead.
  https://github.com/backupsonbackupsrobby-cyber/Prompt

- **backupsonbackupsrobby-cyber/restricted-aibot** (public, placeholder)
  Currently contains only a license file. It is a placeholder and should not be treated as canonical. Start here (`First_project`) for any codex or prompt work.
  https://github.com/backupsonbackupsrobby-cyber/restricted-aibot

- **AiTenetAgency101/ENGINE2** (public, ecosystem runtime — optional context)
  A separate runtime and stack repo positioned as an enterprise security and AI agent framework. Mentioned here for ecosystem awareness only; it is independently maintained and not a dependency of this repo.
  https://github.com/AiTenetAgency101/ENGINE2

For a full tree overview of all repos and their statuses, see `REPO_TREE.md` in this repository.
