from pathlib import Path


def construct_path(to: str) -> Path:
    path = Path(to)
    if not path.exists():
        raise ValueError(f"Could not construct path {to}")

    return path
