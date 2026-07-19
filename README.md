# RISC-V Architectural Parameter Extractor

## Overview

This project extracts architectural parameters from RISC-V ISA specification snippets using a Large Language Model (LLM). It generates structured YAML output and performs a validation pass to improve accuracy by removing unsupported or hallucinated parameters.

The project was developed as part of the Linux Foundation (LFX) Mentorship coding challenge.

---

## Features

- Extracts architectural parameters from RISC-V specification text.
- Produces structured YAML output.
- Uses a second validation stage to verify extracted parameters.
- Reduces hallucinations through prompt engineering.
- Modular and easy-to-extend architecture.

---

## Project Structure

```
riscv-parameter-extractor/
│
├── input/
│   └── snippets.txt
│
├── output/
│   └── parameters.yaml
│
├── prompts/
│   ├── extraction_prompt.txt
│   └── validation_prompt.txt
│
├── src/
│   ├── config.py
│   ├── extractor.py
│   ├── validator.py
│   ├── yaml_writer.py
│   └── main.py
│
├── test_connection.py
├── test_extractor.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository.

```bash
git clone https://github.com/mishtiagrawal02-cloud/riscv-parameter-extractor
cd riscv-parameter-extractor
```

Create a virtual environment.

```bash
python -m venv venv
```

Activate it.

macOS/Linux

```bash
source venv/bin/activate
```

Windows

```bash
venv\Scripts\activate
```

Install dependencies.

```bash
pip install -r requirements.txt
```

---

## Configuration

Create a `.env` file.

```
GROQ_API_KEY=your_api_key
```

The project uses the Groq API with the Llama 3.3 70B Versatile model.

---

## Usage

Run the extraction pipeline.

```bash
python -m src.main
```

The generated YAML will be saved in:

```
output/parameters.yaml
```

---

## Extraction Pipeline

```
Specification
      │
      ▼
Extractor
      │
      ▼
Candidate YAML
      │
      ▼
Validator
      │
      ▼
Validated YAML
      │
      ▼
parameters.yaml
```

---

## Prompt Engineering

The project uses two prompts.

### Extraction Prompt

Responsible for:

- Identifying architectural parameters.
- Extracting descriptions.
- Determining variability.
- Capturing evidence.
- Producing valid YAML.

### Validation Prompt

Responsible for:

- Verifying extracted parameters.
- Removing hallucinations.
- Correcting inaccurate fields.
- Ensuring evidence exists.
- Preserving valid parameters.

---

## Example Output

```yaml
parameters:
  - name: Cache Block Size
    description: The size of a cache block
    type: implementation-specific property
    variability: implementation-specific
    evidence: ...
```

---

## Future Improvements

- Batch processing of specification documents.
- Support for additional LLM providers.
- Automated YAML schema validation.
- Evaluation using benchmark datasets.
- Confidence scoring for extracted parameters.

---

## License

This project was developed for the Linux Foundation (LFX) Mentorship coding challenge.