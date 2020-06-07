from dataclasses import dataclass
from typing import Callable


@dataclass(frozen=True)
class Dependencies:
    pass


def _build_dependencies() -> Callable[[], Dependencies]:
    deps = Dependencies()

    def fn() -> Dependencies:
        return deps

    return fn


get_dependencies = _build_dependencies()
