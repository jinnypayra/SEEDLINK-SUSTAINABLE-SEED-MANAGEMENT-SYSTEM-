import json
import os
from typing import Dict
from exceptions import DataFileCorruptedError, handle_load_error, handle_save_error
from seed_record import SeedRecord

DATA_FILE = "seedlink_data.json"


def load_data() -> Dict:
    """Load saved data"""
    try:
        if not os.path.exists(DATA_FILE):
            return {}

        with open(DATA_FILE, "r") as f:
            data = json.load(f)

        if not isinstance(data, dict):
            raise DataFileCorruptedError("File corrupted")
        return data

    except (json.JSONDecodeError, IOError) as e:
        return handle_load_error(DataFileCorruptedError(str(e)))


def save_data(seed_record: SeedRecord) -> None:
    """
    FLOW: Scan Complete → Save Locally → Retain & Access → END
    """
    try:
        # Save Locally
        data = seed_record.to_dict()
        with open(DATA_FILE, "w") as f:
            json.dump(data, f, indent=2)
        # Retain & Access
        print("💾 Data saved locally → available next time you open the system")
    except IOError as e:
        handle_save_error(e)
