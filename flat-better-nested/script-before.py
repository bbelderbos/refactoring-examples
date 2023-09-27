from typing import Any


def process_data(data: dict[str, Any] | None) -> bool:
    if data is not None:
        if "value" in data:
            value = data["value"]
            if value > 10:
                return True
            else:
                print("Value is too small")
                return False
        else:
            print("No value in data")
            return False
    else:
        print("No data provided")
        return False
