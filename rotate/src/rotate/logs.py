import logging
import subprocess
from datetime import datetime
from pathlib import Path

logger = logging.getLogger(__name__)


def save_logs_and_fs(
    log_path: Path,
    log_path_suffix: str,
    output_path: Path,
    container_name: str,
    container_fs_file: str,
):
    logger.info(f"Saving logs and fs for container {container_name}")
    subprocess.run(
        [
            "tar",
            "czf",
            output_path
            / (
                f"{container_name}_"
                + datetime.now().strftime("%y-%m-%dT%H-%M-%S")
                + ".tar.gz"
            ),
            "--directory",
            log_path,
            f"./{log_path_suffix}",
            "./falco",
            container_fs_file,
            "memory_dump.lime",
            f"container_{container_name}.pid",
        ],
        check=True,
    )


def delete_logs(log_path: Path):
    logger.info("Deleting old logs")
    subprocess.run(["rm", "-rf", log_path], check=True)
