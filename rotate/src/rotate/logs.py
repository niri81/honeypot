import subprocess
from datetime import datetime
from pathlib import Path


def save_logs_and_fs(log_path: Path, output_path: Path):
    subprocess.run(
        [
            "tar",
            "czf",
            output_path / datetime.now().isoformat(),
            "--directory",
            log_path,
        ],
        check=True,
    )
