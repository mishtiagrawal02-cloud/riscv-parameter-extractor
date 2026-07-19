from pathlib import Path

from src.config import client, MODEL_NAME


def load_prompt() -> str:
    """
    Load the extraction prompt from the prompts directory.
    """
    return Path(
        "prompts/extraction_prompt.txt"
    ).read_text(
        encoding="utf-8"
    )


def load_snippets() -> str:
    """
    Load the RISC-V specification snippets.
    """
    return Path(
        "input/snippets.txt"
    ).read_text(
        encoding="utf-8"
    )


def extract_parameters() -> str:
    """
    Extract architectural parameters from the specification
    using the configured language model.
    """

    prompt = load_prompt()
    snippets = load_snippets()

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": "You are an expert RISC-V ISA analyst."
            },
            {
                "role": "user",
                "content": f"{prompt}\n\n{snippets}"
            }
        ],
        temperature=0
    )

    extracted_yaml = response.choices[0].message.content.strip()

    if extracted_yaml.startswith("```yaml"):
        extracted_yaml = extracted_yaml.replace(
            "```yaml",
            "",
            1
        )

    if extracted_yaml.startswith("```"):
        extracted_yaml = extracted_yaml.replace(
            "```",
            "",
            1
        )

    if extracted_yaml.endswith("```"):
        extracted_yaml = extracted_yaml[:-3]

    return extracted_yaml.strip()