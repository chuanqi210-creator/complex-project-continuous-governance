# Project Capability Notes

The Codex repo-scoped skill entry for Complex is:

```text
.agents/skills/complex-runtime/SKILL.md
```

The `.codex/` directory is kept for capability candidates and repository metadata. Do not treat `.codex/skills/` as the official repo skill surface for new Complex workflows.

Before adding any additional local skill or capability note, record:

1. The real project gap it solves.
2. The minimum task that proved it works.
3. What it must not claim or do.
4. Where its output is written back into state, evidence, decisions, loop checks, or delivery records.
5. Whether it changes any protocol rule, template, validation script, or only this local skill layer.

Skills listed in `.codex/shared-skills.json` are capability candidates. They still require environment discovery before use.

For continuous projects, capability notes should support the current operating organization: controller, human interface, literature/data acquisition, model/component, data-code, review/risk, and writing/delivery. Do not add a tool note unless it creates a clearer micro-contract, accepted artifact, review check, or state-compaction path.
