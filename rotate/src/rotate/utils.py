from pathlib import Path


def construct_path(to: str, check_exists: bool = True) -> Path:
    path = Path(to)
    if check_exists and not path.exists():
        raise ValueError(f"Could not construct path {to}")

    return path
