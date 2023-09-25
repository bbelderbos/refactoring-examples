import pytest
from unittest.mock import patch

from script import process_user_input

def test_process_user_input_valid(capfd):
    with patch('builtins.input', return_value="25"):
        process_user_input()
    captured = capfd.readouterr()
    assert captured.out == "25.0 degrees Celsius is equal to 77.0 degrees Fahrenheit.\n"

def test_process_user_input_invalid(capfd):
    with patch('builtins.input', return_value="invalid"):
        process_user_input()
    captured = capfd.readouterr()
    assert captured.out == "Invalid input! Please enter a valid number.\n"

