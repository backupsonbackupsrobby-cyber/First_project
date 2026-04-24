# Ecosystem Repository Map

## Repo tree

```
backupsonbackupsrobby-cyber/
├── First_project           [CANONICAL]  codex framework, generator, doctrine
├── Prompt                  [ARCHIVED]   legacy prompt store (read-only reference)
└── restricted-aibot        [PLACEHOLDER] minimal bot scaffold (not yet active)

AiTenetAgency101/
└── ENGINE2                 [ENGINE]     runtime engine; consumes codex.json;
                                         prompts and rules are intended to live here
```

## Status key

| Status      | Meaning                                                  |
|-------------|----------------------------------------------------------|
| CANONICAL   | Source of truth for codex schema, generator, and doctrine|
| ARCHIVED    | Read-only historical reference; no longer maintained     |
| PLACEHOLDER | Scaffold reserved for future use; not yet active         |
| ENGINE      | Runtime consumer of codex.json; owns prompts/rules       |

## Quick answers

**Which repo is canonical?**
`backupsonbackupsrobby-cyber/First_project`
This repo owns: codex schema, codex_generator.py, detection rules, operational doctrine.

**Where do prompts and rules live?**
In engine repos (runtime consumers), e.g.:
https://github.com/AiTenetAgency101/ENGINE2
This repo remains canonical for the codex framework and generators; prompts and rules are intended to live in the engines that consume codex.json.

**What is `Prompt`?**
https://github.com/backupsonbackupsrobby-cyber/Prompt
Archived legacy prompt store. Kept for historical reference only.

**What is `restricted-aibot`?**
https://github.com/backupsonbackupsrobby-cyber/restricted-aibot
Placeholder bot scaffold. Not yet active.

**What is `ENGINE2`?**
https://github.com/AiTenetAgency101/ENGINE2
Separate ecosystem engine runtime. Consumes codex.json produced by this repo.
