from abc import ABC, abstractmethod

class BlobStorage(ABC):
    @abstractmethod
    def read(self, path: str) -> str:
        pass