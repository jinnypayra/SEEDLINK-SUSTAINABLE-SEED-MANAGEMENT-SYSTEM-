class SDG:
    def __init__(self, crop_name: str):
        self._crop_name = crop_name.strip().lower()

    @property
    def crop_name(self) -> str:
        return self._crop_name

    def get_details(self) -> dict:
        sdg_map = {
            "sunflower": {
                "goal": "SDG 2 - Zero Hunger",
                "description": "Promotes food security, sustainable agriculture, and income generation.",
                "contribution": "High → Drought-resistant, grows in marginal lands, provides oil and food."
            },
            "mango": {
                "goal": "SDG 2 - Zero Hunger\nSDG 13 - Climate Action",
                "description": "Supports nutrition, agroforestry, and carbon sequestration.",
                "contribution": "High → Perennial crop, reduces erosion, provides fruit year-round."
            },
            "rice": {
                "goal": "SDG 2 - Zero Hunger\nSDG 15 - Life on Land",
                "description": "Staple food for billions; supports wetland biodiversity and sustainable land use.",
                "contribution": "Critical → Feeds 50% of global population; improves soil fertility."
            },
            "corn": {
                "goal": "SDG 2 - Zero Hunger\nSDG 12 - Responsible Consumption & Production",
                "description": "Versatile food/feed crop; supports sustainable farming practices.",
                "contribution": "Essential → Used for food, feed, and raw materials; crop rotation friendly."
            }
        }
        return sdg_map.get(self._crop_name, {
            "goal": "SDG 2 - Zero Hunger",
            "description": "Supports sustainable food production and local food systems.",
            "contribution": "Moderate → Contributes to community food supply and livelihood."
        })

    def __str__(self) -> str:
        details = self.get_details()
        return f"SDG({self._crop_name} → {details['goal']})"