import pytest
from src.rearrange_string import rearrange_string


def rearrange_string():
    string = "AbC123DeF"
    result = rearrange_string(string)
    assert result == "fedcba", "the answer is wrong"
