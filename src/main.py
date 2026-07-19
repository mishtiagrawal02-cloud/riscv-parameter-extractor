import logging
from pathlib import Path

from src.extractor import extract_parameters
from src.validator import validate_parameters
from src.yaml_writer import save_yaml

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


def main() -> None:
    """
    Execute the complete extraction and validation pipeline.
    """

    logger.info("Starting parameter extraction...")

    yaml_output = extract_parameters()

    specification = Path(
        "input/snippets.txt"
    ).read_text(
        encoding="utf-8"
    )

    validated_yaml = validate_parameters(
        specification,
        yaml_output
    )

    save_yaml(validated_yaml)

    logger.info("Validation completed.")
    logger.info("Extraction completed successfully.")


if __name__ == "__main__":
    main()