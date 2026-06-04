class Crop:
    def __init__(self, name: str, seed_id: str, resilience: str, use: str):
        self._name = name
        self._seed_id = seed_id
        self._resilience = resilience
        self._use = use

    @property
    def name(self) -> str:
        return self._name

    @property
    def seed_id(self) -> str:
        return self._seed_id

    @property
    def resilience(self) -> str:
        return self._resilience

    @property
    def use(self) -> str:
        return self._use

    def __str__(self) -> str:
        return f"Crop({self._name}, ID={self._seed_id})"
