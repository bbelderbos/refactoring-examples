def get_user_input() -> float | None:
    user_input = input("Enter a temperature in Celsius: ")
    try:
        celsius = float(user_input)
        return celsius
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return None


def convert_celsius_to_fahrenheit(celsius: float) -> float:
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


def show_result(celsius: float, fahrenheit: float) -> None:
    print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")


def process_user_input():
    celsius = get_user_input()
    if celsius is None:
        return
    fahrenheit = convert_celsius_to_fahrenheit(celsius)
    show_result(celsius, fahrenheit)


if __name__ == "__main__":
    process_user_input()
