class InvalidSeedError(Exception):
    pass


class DataFileCorruptedError(Exception):
    pass


# --- Error Handlers ---
def handle_save_error(error: Exception) -> None:
    print(f"⚠️ Save Error: {error}")


def handle_load_error(error: Exception) -> dict:
    print(f"⚠️ Load Error: {error}")
    return {}


def handle_scan_error(error: Exception) -> None:
    print(f"⚠️ Scan Error: {error}")
