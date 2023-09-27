from script import process_data


def test_none_case():
    assert process_data(None) is False


def test_empty_dict():
    assert process_data({}) is False


def test_lte_10_value():
    assert process_data({"value": 5}) is False


def test_eq_10_value():
    assert process_data({"value": 10}) is False


def test_gt_10_value():
    assert process_data({"value": 15}) is True
