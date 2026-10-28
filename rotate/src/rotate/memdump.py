import logging
import shutil
import subprocess
from pathlib import Path

logger = logging.getLogger(__name__)


def dump_memory(log_path: Path, memdump_filename: str):
    if not shutil.which("avml"):
        logger.error(
            "Could not find binary `avml` in path, will not capture memory dump"
        )
        return

    logger.info(f"Will now dump memory and save to file {memdump_filename}")

    subprocess.run(["avml", "acquire", memdump_filename], cwd=log_path, check=True)
