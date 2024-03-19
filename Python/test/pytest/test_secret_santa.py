import pytest
from src.secret_santa import secret_santa


@pytest.mark.parametrize(
    "players",
    [
        (["Valentina", "Jorge", "Luis", "Miguel", "Sofia"]),
        (["Alice", "Bob", "Charlie"]),
        (["David", "Emily", "Frank", "George"]),
    ],
)
def test_secret_santa(players):
    pairs = secret_santa(players)
    assert len(pairs) == len(players), "Número incorrecto de pares generados"
    for pair in pairs:
        giver, receiver = pair
        assert giver != receiver, "El dador y el receptor son iguales"
