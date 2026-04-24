# Repository Tree

Single source of truth for all repositories in this ecosystem.
Last updated: 2026-04-24

---

## Where to Start

If you are new, start here:
https://github.com/backupsonbackupsrobby-cyber/First_project

This is the canonical repo for the ESP codex framework, codex generators, and detection rules.

---

## Repository Map

```
backupsonbackupsrobby-cyber/
├── First_project           [CANONICAL] [active] [public]
│   Purpose : ESP codex framework; codex generator/enhancer scripts;
│             Sigma-like detection rules (e.g. RVL_Local_Malignancy_Detected).
│   Start   : README.md → codex_generator.py / codex_input.yaml
│   URL     : https://github.com/backupsonbackupsrobby-cyber/First_project
│
├── vs-studioPROMPT         [active] [private]
│   Purpose : VS Code workspace for prompt and rule authoring.
│             Drafts, rule-spec files (architexture, layers), and AI/engine/stability dirs.
│             Source of rule definitions that feed into First_project.
│   Note    : Private — not publicly accessible.
│   URL     : https://github.com/backupsonbackupsrobby-cyber/vs-studioPROMPT
│
├── Prompt                  [archived] [legacy] [public]
│   Purpose : Early concept scratchpad / snippet dump.
│             Contains fragments like root_os.json, codex53.ts placeholders.
│             Not canonical. Read-only (archived).
│   Note    : Do not use as a starting point. Refer to First_project instead.
│   URL     : https://github.com/backupsonbackupsrobby-cyber/Prompt
│
└── restricted-aibot        [placeholder] [public]
    Purpose : Placeholder repository. Currently contains only a LICENSE file.
              No active code or documentation.
    Note    : Not canonical. If you landed here from a link, go to First_project.
    URL     : https://github.com/backupsonbackupsrobby-cyber/restricted-aibot

AiTenetAgency101/
└── ENGINE2                 [active] [public] [separate ecosystem]
    Purpose : Runtime and stack repo — "Quantum Lantern Protocol" enterprise
              security, satellite-verified state, and AI agent framework.
              Independently maintained; not a dependency of First_project.
    Note    : Mentioned for ecosystem awareness only. Maintained by AiTenetAgency101.
    URL     : https://github.com/AiTenetAgency101/ENGINE2
```

---

## Status Key

| Status      | Meaning                                              |
|-------------|------------------------------------------------------|
| CANONICAL   | Authoritative source of truth; start here            |
| active      | Actively maintained                                  |
| archived    | Read-only; no longer maintained; legacy reference    |
| placeholder | Repo exists but has no meaningful content yet        |
| private     | Not publicly accessible                              |

---

## Quick Answers

**Which repo is canonical?**
`backupsonbackupsrobby-cyber/First_project`
https://github.com/backupsonbackupsrobby-cyber/First_project

**Where do prompts and rules live?**
`backupsonbackupsrobby-cyber/vs-studioPROMPT` (private authoring workspace)
https://github.com/backupsonbackupsrobby-cyber/vs-studioPROMPT

**Is `Prompt` still in use?**
No. It is archived (read-only). Use `First_project` for all active codex work.

**Is `restricted-aibot` canonical?**
No. It is a placeholder. Use `First_project`.
