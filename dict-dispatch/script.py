import operator


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


OPERATIONS = {"add": add, "subtract": subtract, "multiply": multiply, "divide": divide}


def operation_result(a, b, operation):
    if operation not in OPERATIONS:
        raise ValueError("Unknown operation")
    return OPERATIONS[operation](a, b)


# as per video, but I generally use pytest
assert operation_result(10, 5, "divide") == 2.0
assert operation_result(10, 5, "multiply") == 50
assert operation_result(10, 5, "add") == 15
assert operation_result(10, 5, "subtract") == 5
