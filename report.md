# LFX Coding Challenge Report

## Project Objective

The objective of this project is to automatically extract architectural parameters from RISC-V ISA specification snippets using a Large Language Model (LLM). The extracted information is converted into a structured YAML representation suitable for downstream processing.

---

# LLM Selection

The project uses Groq's hosted Llama 3.3 70B Versatile model.

Reasons for selecting this model include:

- Fast inference.
- Strong instruction-following capability.
- Good structured output generation.
- Reliable handling of technical documentation.
- Easy API integration.

---

# Prompt Development

The extraction prompt instructs the model to:

- Identify architectural parameters.
- Produce structured YAML.
- Extract descriptions.
- Identify parameter variability.
- Include constraints.
- Quote supporting evidence.

The prompt explicitly instructs the model not to invent information and to return only YAML.

---

# Prompt Refinement

During development, the prompt was refined by:

- Adding an explicit YAML schema.
- Requiring evidence for every parameter.
- Restricting responses to YAML only.
- Using deterministic inference with temperature set to zero.
- Improving wording to reduce ambiguity.

---

# Validation Strategy

A second LLM call validates the extracted YAML.

The validator:

- Compares extracted parameters against the original specification.
- Removes unsupported parameters.
- Corrects inaccurate fields.
- Preserves valid parameters.
- Ensures every parameter includes supporting evidence.

This two-stage pipeline improves extraction quality and reduces hallucinations.

---

# Hallucination Handling

Several techniques were used to reduce hallucinations.

- Explicit prompt instructions.
- Evidence-based extraction.
- Deterministic generation.
- Independent validation stage.
- Preservation of only supported parameters.

These techniques improve reliability while maintaining structured output.

---

# Limitations

Current limitations include:

- Single specification input.
- Dependence on LLM output quality.
- No automatic YAML schema validation.
- No quantitative evaluation metrics.

---

# Future Work

Potential improvements include:

- Processing complete RISC-V specifications.
- Automatic YAML validation.
- Confidence scoring.
- Benchmark-based evaluation.
- Support for multiple LLM providers.

---

# Conclusion

The developed system successfully extracts architectural parameters from RISC-V specification snippets, validates the generated output, and produces structured YAML. The modular design and two-stage extraction pipeline make the system suitable for further extension and experimentation.