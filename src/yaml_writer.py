import logging
from pathlib import Path

logger = logging.getLogger(__name__)

OUTPUT_DIR = Path("output")
OUTPUT_FILE = OUTPUT_DIR / "parameters.yaml"


def save_yaml(text: str) -> None:
    """
    Save validated parameters to a YAML file.
    """

    OUTPUT_DIR.mkdir(exist_ok=True)

    OUTPUT_FILE.write_text(
        text,
        encoding="utf-8"
    )

    logger.info(f"Saved YAML to {OUTPUT_FILE}")