# agent-customization Skill: Create a `SKILL.md`

This skill captures the pattern for helping the user define a new Copilot skill by writing a `SKILL.md` file.  It is scoped to any workspace where the user wants to codify a repeating workflow or checklist.

## When to invoke this skill

- The user asks you to "make a skill" or "write a SKILL.md".
- They are following a multi‑step procedural workflow that could be reused.
- They need guidance on documenting a process for future automation.

## Outcome

Produce a complete, workspace‑scoped `SKILL.md` document that:

1. Describes the workflow or decision tree extracted from the conversation.
2. Lists step‑by‑step instructions, branching points, and quality criteria.
3. Mentions any clarifying questions to ask the user when the workflow is ambiguous.
4. Suggests example prompts and related skills to create next.

## Workflow

1. **Review conversation history.**
   - Scan recent messages for a recurring process, checklist, or multi‑step decision flow.
   - If none exists, plan to ask clarifying questions (see below).

2. **Extract the steps.**
   - Write the sequence of actions the user has followed.
   - Note any conditional branches or decision criteria.
   - Capture completion checks or success criteria.

3. **Draft the skill text.**
   - Use a clear, formal tone.
   - Include frontmatter if required by repository conventions (e.g. `applyTo` patterns).
   - Structure the document with headings: When to use, Outcome, Steps, Examples.

4. **Identify ambiguities.**
   - If the workflow isn’t obvious, generate clarifying questions to ask the user:
     - "What should the skill produce?"
     - "Is this intended for this workspace or your personal use?"
     - "Do you want a simple checklist or a detailed, branched procedure?"

5. **Iterate with the user.**
   - Present the draft and invite feedback.
   - Refine until the user is satisfied.
   - Save the final `SKILL.md` in the workspace (at project root or `/skills` folder).

6. **Finish with examples.**
   - Provide sample prompts the user can try with the new skill.
   - Suggest related skills they might create next (e.g. "create a prompt template", "debug a skill").

## Quality criteria

- The instructions should be actionable and self‑contained.
- The skill must clearly separate 
  - the identification phase, 
  - the extraction phase, and 
  - the writing phase.
- Prompts and examples should illustrate typical uses.
- The skill text should be generic enough to apply to most simple workflows, but give pointers for complexity (branches or loops).

## Example prompts

- "Help me write a new skill for running security audits."
- "There's a repetitive process I follow when debugging build errors; make a skill for that."
- "How do I document the review checklist workflow as a SKILL.md?" 

## Related skills to consider

- `prompt-creation`: guide for crafting `.prompt.md` templates.
- `agent-review`: internal review and testing workflow for new agents.
- `repository-scaffolding`: set up project structure for skills or instructions.

---

This file itself is an instance of the skill it describes; use the steps above when you need to author another `SKILL.md`.