# Language Model Contract

All evaluated workflow conditions use the same provider-neutral language model
interface.

The shared contract separates workflow design from provider-specific API code.
A model call receives a sequence of messages together with the requested
temperature and output-token limit.

Each response records:

- generated text;
- provider-reported input tokens;
- provider-reported output tokens;
- finish reason when available;
- provider response identifier when available.

Provider-native usage values are preserved rather than estimated when the
provider reports them.

Model-call latency is measured by the execution logging layer rather than by the
model contract.

This interface does not define the final benchmark model, prompt, or parameter
values. Those settings will be frozen separately before the full benchmark.

Using the same model contract across B0, B1, and G1 supports consistent resource
measurement and reduces implementation differences unrelated to the research
comparison.
