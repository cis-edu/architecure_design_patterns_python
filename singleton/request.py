from typing import Optional


class Requests:
    _instance: Optional["Requests"] = None
    count: int
    last_path: Optional[str]
    last_seconds: Optional[float]

    def __new__(cls) -> "Requests":
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.count = 0
            cls._instance.last_path = None
            cls._instance.last_seconds = None
        return cls._instance

    @classmethod
    def get_instance(cls) -> "Requests":
        return cls()
