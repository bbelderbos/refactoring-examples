def calculate_yearly_bonus(salary: float) -> float:
    # 0.1 represents the 10% bonus rate
    # 12 represents the number of months in a year
    return salary * 0.1 * 12


salary = 5000
bonus = calculate_yearly_bonus(salary)
print(f"The yearly bonus for a monthly salary of ${salary} is: ${bonus}")

assert bonus == 6000
