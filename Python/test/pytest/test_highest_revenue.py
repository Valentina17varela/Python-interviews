import pytest
from src.highest_revenue import highest_revenue_item


def test_highest_revenue_item():
    data = """111, 5
    111, 5
    111, 5 
    222, 3
    333, 6
    333, 6"""
    assert highest_revenue_item(data) == 111

    data_diff_prices = """111, 5
    111, 6
    111, 5
    222, 3
    333, 6
    333, 6"""
    assert highest_revenue_item(data_diff_prices) == -1

    data_negative_revenue = """111, -5
    111, -5
    111, -5
    222, -3
    333, -6
    333, -6"""
    assert highest_revenue_item(data_negative_revenue) == -1

    data_empty = ""
    assert highest_revenue_item(data_empty) == -1

    data_single_sale = "999, 10"
    assert highest_revenue_item(data_single_sale) == 999

    data_multiple_products = """111, 5
    111, 5
    111, 5
    222, 3
    333, 6
    333, 6
    444, 8
    444, 8
    444, 8"""
    assert highest_revenue_item(data_multiple_products) == 444
