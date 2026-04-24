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
├── First_project                [CANONICAL] [active] [public]
│   Purpose : ESP codex framework; codex generator/enhancer scripts;
│             Sigma-like detection rules (e.g. RVL_Local_Malignancy_Detected).
│   Start   : README.md → codex_generator.py / codex_input.yaml
│   URL     : https://github.com/backupsonbackupsrobby-cyber/First_project
│
├── Prompt                       [archived] [legacy] [public]
│   Purpose : Early concept scratchpad / snippet dump.
│             Contains fragments like root_os.json, codex53.ts placeholders.
│             Not canonical. Read-only (archived).
│   Note    : Do not use as a starting point. Refer to First_project instead.
│   URL     : https://github.com/backupsonbackupsrobby-cyber/Prompt
│
├── restricted-aibot             [placeholder] [public]
│   Purpose : Placeholder repository. Currently contains only a LICENSE file.
│             No active code or documentation.
│   Note    : Not canonical. If you landed here from a link, go to First_project.
│   URL     : https://github.com/backupsonbackupsrobby-cyber/restricted-aibot
│
└── atmospheric-truth-layer      [active] [public] [witness/anchors/attestation]
    Purpose : Witness, attestation, and anchor artifacts layer.
              Contains ANCHOR.json, WITNESS-ANCHORS.md, and multiple *-anchor.json files.
    Note    : Mentioned for ecosystem awareness; not a dependency of First_project.
    URL     : https://github.com/backupsonbackupsrobby-cyber/atmospheric-truth-layer

AiTenetAgency101/
└── ENGINE2                      [active] [public] [separate ecosystem]
    Purpose : Runtime and stack repo — "Quantum Lantern Protocol" enterprise
              security, satellite-verified state, and AI agent framework.
              Independently maintained; not a dependency of First_project.
    Note    : Mentioned for ecosystem awareness only. Maintained by AiTenetAgency101.
    URL     : https://github.com/AiTenetAgency101/ENGINE2
```

---

## Status Key

| Status              | Meaning                                              |
|---------------------|------------------------------------------------------|
| CANONICAL           | Authoritative source of truth; start here            |
| active              | Actively maintained                                  |
| archived            | Read-only; no longer maintained; legacy reference    |
| placeholder         | Repo exists but has no meaningful content yet        |
| witness/anchors     | Stores attestation and anchor artifacts              |

---

## Quick Answers

**Which repo is canonical?**
`backupsonbackupsrobby-cyber/First_project`
https://github.com/backupsonbackupsrobby-cyber/First_project

**Where do prompts and rules live?**
Runtime prompts and engine-specific rule packs should live in engine repos (runtime consumers), for example:
https://github.com/AiTenetAgency101/ENGINE2

This repo (`First_project`) remains canonical for the codex framework + generators and for detection-rule definitions inside the codex contract.

**Is `Prompt` still in use?**
No. It is archived (read-only). Use `First_project` for all active codex work.

**Is `restricted-aibot` canonical?**
No. It is a placeholder. Use `First_project`.

**What is `atmospheric-truth-layer`?**
A witness/attestation and anchor artifacts repo (ANCHOR.json, WITNESS-ANCHORS.md, *-anchor.json files).
Mentioned for ecosystem awareness; not a dependency of First_project.
https://github.com/backupsonbackupsrobby-cyber/atmospheric-truth-layer
