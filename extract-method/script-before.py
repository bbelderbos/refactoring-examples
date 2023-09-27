def process_user_input():
    # 1. Validate User Input
    user_input = input("Enter a temperature in Celsius: ")
    try:
        celsius = float(user_input)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
        return

    # 2. Transform Input
    fahrenheit = (celsius * 9 / 5) + 32

    # 3. Respond to User
    print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")


if __name__ == "__main__":
    process_user_input()
