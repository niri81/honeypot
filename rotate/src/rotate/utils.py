from pathlib import Path


def construct_path(to: str) -> Path:
    path = Path(to)
    if not path.exists():
        raise ValueError("Could not find config file config.toml")

    return path
