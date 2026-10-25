import logging
import subprocess
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)


def save_logs_and_fs(log_path: Path, output_path: Path):
    logger.info("Saving logs and fs")
    subprocess.run(
        [
            "tar",
            "czf",
            output_path / (datetime.now().strftime("%y-%m-%dT%H-%M-%S") + ".tar.gz"),
            "--directory",
            log_path,
            ".",
        ],
        check=True,
    )


def delete_logs(log_path: Path):
    logger.info("Deleting old logs")
    subprocess.run(["rm", "-rf", log_path], check=True)
