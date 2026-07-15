# Evidence Fill Minimal Runtime Example

This example shows the smallest useful Complex runtime for a task where the model, metric, and evidence table are already fixed. It should not trigger broad model discovery.

Use this example when a new project says:

```text
模型和指标已经确定，只需要补齐来源、验证和交付说明。
```

Files:

- `state.md`: current basis, project nature, autonomy boundary, and next route.
- `evidence.md`: evidence levels and claim boundaries.
- `loop.md`: a short evidence-check loop.
- `delivery.md`: human-readable delivery contract.

## Four-Layer Boundary

- Prompt Contract: fixed model, metric, claim boundary, and evidence-ready completion criteria.
- Context Working Set: current sources and claim gaps; broad framing alternatives are excluded.
- Runtime Harness: source access, extraction tools, citation checks, and reproducible evidence paths are assumed inspectable.
- Progress Loop: completes when the selected claim has attributable evidence or an explicit no-hit boundary, not when a search query finishes.

This example does not prove the sources are externally validated or that every evidence task should avoid model discovery.
