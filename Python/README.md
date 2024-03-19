# Python Challenges

## Secret Santa
Given a list of players, pair up players so that:

- Each player gives a gift once
- Each player receives a gift once
- No player gives a gift to themselves
- Selection is random

Input: ['Valentina', 'Jorge', 'Luis', 'Miguel', 'Sofia']
<br>
Output: [['Valentina', 'Jorge'], ['Jorge', 'Luis'], ['Luis', 'Miguel'], ['Miguel', 'Sofia'], ['Sofia', 'Valentina']]

👩🏻‍💻[Solution](src/secret_santa.py)
<br>
🕵🏻 Test: [Pytest](test/pytest/test_secret_santa.py) [Unittest](test/unittest/test_secret_santa_unit.py)


## Online Cloud Reading Application
(Like Kindle)

- Users have a library of books that they can add to or remove from
- Users can set a book from their library as active
- The reading app should keep track of the current page the user is on
- The reading app only displays 1 page at a time in the active book

👩🏻‍💻[Solution](src/reading_app.py)
<br>
🕵🏻 Test: [Pytest](test/pytest/test_reading_app.py) [Unittest](test/unittest/test_reading_app_unit.py)