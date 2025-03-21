import os
import traceback
from typing import Optional


class CleanUpFile:
    def __init__(self, filename: str) -> None:
        self.filename = filename

    def __enter__(self) -> "CleanUpFile":
        return self

    def __exit__(self,
                 exc_type: type,
                 exc_value: Exception,
                 traceback: Optional[traceback]) \
            -> None:
        if os.path.exists(self.filename):
            os.remove(self.filename)
            print(f"{self.filename} has been deleted.")
