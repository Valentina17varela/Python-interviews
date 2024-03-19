# Python Challenges

## 1. Secret Santa
Given a list of players, pair up players so that:

- Each player gives a gift once
- Each player receives a gift once
- No player gives a gift to themselves
- Selection is random

Input: ['Valentina', 'Jorge', 'Luis', 'Miguel', 'Sofia']
<br>
Output: [['Valentina', 'Jorge'], ['Jorge', 'Luis'], ['Luis', 'Miguel'], ['Miguel', 'Sofia'], ['Sofia', 'Valentina']]

[ 👩🏻‍💻 Solution](src/secret_santa.py)
<br>
🕵🏻 Test: [Pytest](test/pytest/test_secret_santa.py) [Unittest](test/unittest/test_secret_santa_unit.py)