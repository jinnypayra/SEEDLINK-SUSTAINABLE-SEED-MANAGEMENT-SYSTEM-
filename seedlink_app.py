from datetime import date
from crop import Crop
from exchange import Exchange
from seed_record import SeedRecord
from validation import is_seed
from storage import load_data, save_data
from exceptions import InvalidSeedError, handle_scan_error
from sdg import SDG  # ✅ Import separate SDG


class SeedLinkApp:
    def __init__(self):
        # Feature 2: Simple Interface → Display Layout
        print("="*40)
        print("       SEEDLINK SYSTEM")
        print(" Sustainable Seed Management")
        print("="*40)
        self._seed_record = None
        # Load existing data
        data = load_data()
        if data:
            self._seed_record = self._build_record(data)

    def _build_record(self, raw: dict) -> SeedRecord:
        crop_data = raw["crop"]
        exchange_data = raw["exchange"]

        crop = Crop(
            name=crop_data["name"],
            seed_id=crop_data["seed_id"],
            resilience=crop_data["resilience"],
            use=crop_data["use"]
        )

        exchange = Exchange(
            crop_name=exchange_data["crop_name"],
            source=exchange_data["source"],
            destination=exchange_data["destination"],
            date=date.fromisoformat(exchange_data["date"])
        )

        # ✅ FIX: If old file has NO 'sdg' key → create automatically
        if "sdg" in raw:
            sdg = SDG(crop_data["name"])
        else:
            sdg = SDG(crop_data["name"])

        return SeedRecord(crop, exchange, sdg)

    def scan(self, input_name: str) -> bool:
        """
        Feature 2: Input + Scan Button → Easy Use
        Feature 5: Detect Action → Show Messages → Guide User
        """
        try:
            # Feature 5: Detect Action
            print("\n🔍 Scanning...")
            is_seed(input_name)  # Feature 1 flow

            # Generate data
            seed_id = "PH-001"
            resilience = f"Drought:{70 + len(input_name)%30}% | Flood:{60 + len(input_name)%25}%"
            use = ["Cooking", "Planting", "Snack"][len(input_name)%3]

            crop = Crop(input_name, seed_id, resilience, use)
            exchange = Exchange(
                crop_name=input_name,
                source="Local Farmers Co-op",
                destination=["Philippines", "Thailand", "Vietnam"][len(input_name)%3],
                date=date.today()
            )

            # ✅ CREATE SDG SEPARATELY
            sdg = SDG(input_name)

            self._seed_record = SeedRecord(crop, exchange, sdg)
            save_data(self._seed_record)  # Feature 4 flow

            # Feature 5: Show Messages
            print(f"✅ SUCCESS: '{input_name}' scanned and saved!")
            return True

        except InvalidSeedError as e:
            # Feature 5: Show Messages → Guide User
            handle_scan_error(e)
            print("💡 GUIDE: Please enter a valid seed only (e.g. Sunflower, Mango, Corn)")
            return False

    def update_display(self) -> None:
        """
        Feature 3: After Scan → Load All Info → Scrollable View → END
        """
        print("\n" + "="*40)
        print("📋 SCANNED SEED DETAILS")
        print("="*40)

        if not self._seed_record or not self._seed_record.has_record():
            print("📂 No data available. Scan a seed first.")
            print("="*40 + "\n")
            return

        # Load All Info
        crop = self._seed_record.crop
        ex = self._seed_record.exchange
        sdg_details = self._seed_record.sdg.get_details()  # ✅ Separate SDG data

        # Crop & Exchange Info
        print(f"Name      : {crop.name}")
        print(f"ID        : {crop.seed_id}")
        print(f"Resilience: {crop.resilience}")
        print(f"Use       : {crop.use}")
        print("-"*40)
        print(f"From      : {ex.source}")
        print(f"To        : {ex.destination}")
        print(f"Date      : {ex.date}")
        print("-"*40)

        # ✅ SDG DISPLAYED AS COMPLETELY SEPARATE SECTION
        print("🌱 SUSTAINABLE DEVELOPMENT GOAL")
        print(f"Goal      : {sdg_details['goal']}")
        print(f"About     : {sdg_details['description']}")
        print(f"Contribution: {sdg_details['contribution']}")
        print("-"*40)

        print("🔽 [Scroll up/down to view all details]")
        print("="*40 + "\n")


# ------------------------------
# RUN SYSTEM
# ------------------------------
if __name__ == "__main__":
    app = SeedLinkApp()

    while True:
        # Feature 2: Simple Interface → Input + Scan Button
        print("\n--- MENU ---")
        print("1. Scan Seed")
        print("2. Show Details")
        print("3. Exit")
        choice = input("Select option: ")

        if choice == "1":
            name = input("Enter seed name: ")
            app.scan(name)
        elif choice == "2":
            app.update_display()
        elif choice == "3":
            print("🔒 System closed.")
            break
        else:
            # Feature 5: User Feedback
            print("❌ Invalid choice → Please select 1, 2 or 3")
