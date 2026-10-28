class Requests:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.count = 0
            cls._instance.last_path = None
            cls._instance.last_seconds = None
        return cls._instance

    @classmethod
    def get_instance(cls):
        return cls()

    def to_dict(self):
        return {
            "count": self.count,
            "last_path": self.last_path,
            "last_seconds": self.last_seconds,
        }
