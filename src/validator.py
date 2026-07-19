from pathlib import Path

from src.config import client, MODEL_NAME


def load_validation_prompt() -> str:
    """
    Load the validation prompt from the prompts directory.
    """
    return Path(
        "prompts/validation_prompt.txt"
    ).read_text(
        encoding="utf-8"
    )


def validate_parameters(
    specification: str,
    yaml_output: str
) -> str:
    """
    Validate extracted parameters against the
    original RISC-V specification.
    """

    prompt = load_validation_prompt()

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {
                "role": "system",
                "content": "You are an expert RISC-V ISA reviewer."
            },
            {
                "role": "user",
                "content": f"""
{prompt}

Original Specification:

{specification}

Candidate YAML:

{yaml_output}
"""
            }
        ],
        temperature=0
    )

    validated_yaml = response.choices[0].message.content.strip()

    if validated_yaml.startswith("```yaml"):
        validated_yaml = validated_yaml.replace(
            "```yaml",
            "",
            1
        )

    if validated_yaml.startswith("```"):
        validated_yaml = validated_yaml.replace(
            "```",
            "",
            1
        )

    if validated_yaml.endswith("```"):
        validated_yaml = validated_yaml[:-3]

    return validated_yaml.strip()