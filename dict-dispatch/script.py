def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


# could use the `operator` module here but using functions
# to better illustrate the dictionary dispatch pattern
OPERATIONS = {"add": add, "subtract": subtract, "multiply": multiply, "divide": divide}


def operation_result(a, b, operation):
    if operation not in OPERATIONS:
        raise ValueError("Unknown operation")
    return OPERATIONS[operation](a, b)
