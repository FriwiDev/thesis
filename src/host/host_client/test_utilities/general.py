from abc import ABC, abstractmethod
from typing import Any


class TestUtility(ABC):
    @abstractmethod
    def run(self) -> Any:
        pass
