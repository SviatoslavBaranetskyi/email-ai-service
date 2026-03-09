from app.storage.blob_storage import BlobStorage
from pathlib import Path

class LocalBlobStorage(BlobStorage):
    def __init__(self, base_path: str = "blobs"):
        self.base_path = Path(base_path)

    def read(self, path: str) -> str:
        file_path = self.base_path / path
        if not file_path.exists():
            raise FileNotFoundError(f"File {file_path} was not found in local storage.")
        return file_path.read_text(encoding="utf-8")