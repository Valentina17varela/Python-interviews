import unittest
from src.secret_santa import secret_santa

"""
python3 -m unittest test_secret_santa_unit.py
"""


class TestSecretSanta(unittest.TestCase):
    def test_secret_santa(self):
        players = ["Valentina", "Jorge", "Luis", "Miguel", "Sofia"]
        pairs = secret_santa(players)
        self.assertEqual(
            len(pairs), len(players), "Número incorrecto de pares generados"
        )
        for pair in pairs:
            giver, receiver = pair
            self.assertNotEqual(giver, receiver, "El dador y el receptor son iguales")


if __name__ == "__main__":
    unittest.main()
