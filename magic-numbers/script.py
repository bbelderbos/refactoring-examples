BONUS_PERCENTAGE = 0.1
MONTHS_IN_YEAR = 12


def calculate_yearly_bonus(salary: float) -> float:
    return salary * BONUS_PERCENTAGE * MONTHS_IN_YEAR


salary = 5000
bonus = calculate_yearly_bonus(salary)
print(f"The yearly bonus for a monthly salary of ${salary} is: ${bonus}")

assert bonus == 6000
