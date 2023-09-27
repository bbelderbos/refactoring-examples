from typing import Any


def process_data(data: dict[str, Any] | None) -> bool:
    if data is None:
        print("No data provided")
        return False

    if "value" not in data:
        print("No value in data")
        return False

    return data["value"] > 10
