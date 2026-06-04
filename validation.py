import re
from exceptions import InvalidSeedError


def is_seed(input_text: str) -> bool:
    """
    FLOW: Start → Receive Input → Verify → Accept & Reject → END
    """
    # Receive Input
    if not input_text.strip():
        raise InvalidSeedError("Input cannot be empty")

    clean_text = re.sub(r'\s+', ' ', input_text.strip()).lower()

    # Verify
    invalid_words = [
        "pillow", "bed", "chair", "table", "phone", "laptop", "tv",
        "book", "pen", "bag", "shoe", "bread", "milk", "juice", "car"
    ]
    for word in invalid_words:
        if word in clean_text:
            # Reject
            raise InvalidSeedError(f"'{input_text}' is NOT a seed → REJECTED")

    seed_keywords = ["seed", "sunflower", "mango", "apple", "corn", "rice"]
    if any(key in clean_text for key in seed_keywords):
        # Accept
        return True

    # Verify unknown items
    confirm = input(f"Is '{input_text}' a seed? (y/n): ").strip().lower()
    if confirm != "y":
        # Reject
        raise InvalidSeedError(f"'{input_text}' → REJECTED by user")
    # Accept
    return True
