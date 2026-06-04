from datetime import date


class Exchange:
    def __init__(self, crop_name: str, source: str, destination: str, date: date):
        self._crop_name = crop_name
        self._source = source
        self._destination = destination
        self._date = date

    @property
    def crop_name(self) -> str:
        return self._crop_name

    @property
    def source(self) -> str:
        return self._source

    @property
    def destination(self) -> str:
        return self._destination

    @property
    def date(self) -> date:
        return self._date

    def __str__(self) -> str:
        return f"Exchange({self._crop_name}, From={self._source}, To={self._destination})"
