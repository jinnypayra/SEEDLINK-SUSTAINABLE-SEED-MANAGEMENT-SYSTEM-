from crop import Crop
from exchange import Exchange
from sdg import SDG  # ✅ Imports our separate SDG file


class SeedRecord:
    def __init__(self, crop: Crop, exchange: Exchange, sdg: SDG = None):
        self._crop = crop
        self._exchange = exchange
        # ✅ If SDG is missing (old data), create it automatically
        self._sdg = sdg if sdg is not None else SDG(crop.name)

    @property
    def crop(self) -> Crop:
        return self._crop

    @property
    def exchange(self) -> Exchange:
        return self._exchange

    @property
    def sdg(self) -> SDG:
        return self._sdg

    def has_record(self) -> bool:
        return self._crop is not None and self._exchange is not None

    def to_dict(self) -> dict:
        return {
            "crop": {
                "name": self._crop.name,
                "seed_id": self._crop.seed_id,
                "resilience": self._crop.resilience,
                "use": self._crop.use
            },
            "exchange": {
                "crop_name": self._exchange.crop_name,
                "source": self._exchange.source,
                "destination": self._exchange.destination,
                "date": str(self._exchange.date)
            },
            # ✅ SDG saved as COMPLETELY SEPARATE block
            "sdg": self._sdg.get_details()
        }

    def __str__(self) -> str:
        return f"SeedRecord[{self._crop} | {self._exchange} | {self._sdg}]"
