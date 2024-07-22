from script import operation_result

import pytest


@pytest.mark.parametrize(
    "a, b, operation, expected",
    [
        (10, 5, "divide", 2.0),
        (10, 5, "multiply", 50),
        (10, 5, "add", 15),
        (10, 5, "subtract", 5),
    ],
)
def test_operation_result(a, b, operation, expected):
    assert operation_result(a, b, operation) == expected
