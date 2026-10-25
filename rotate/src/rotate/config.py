from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Self

import yaml


@dataclass(frozen=True, slots=True)
class Config:
    config: dict[str, Any] = field(default_factory=dict)

    @classmethod
    def from_yaml(cls, path: str | Path) -> Self:
        with open(path, "rb") as f:
            raw = yaml.safe_load(f)
        return cls(config=raw)

    def get(self, arg, /) -> Any:
        return self.config.get(arg)
