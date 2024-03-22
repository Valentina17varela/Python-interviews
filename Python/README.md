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

<br><br>

## Online Cloud Reading Application
(Like Kindle)

- Users have a library of books that they can add to or remove from
- Users can set a book from their library as active
- The reading app should keep track of the current page the user is on
- The reading app only displays 1 page at a time in the active book

👩🏻‍💻[Solution](src/reading_app.py)
<br>
🕵🏻 Test: [Pytest](test/pytest/test_reading_app.py) [Unittest](test/unittest/test_reading_app_unit.py)

<br><br>

## Rearrange String

Given a string, write a function named rearrange_string that performs the following:
- Removes all digits.
- Converts all uppercase letters to lowercase.
- Reverses the string.

👩🏻‍💻[Solution](src/rearrange_string.py)
<br>
🕵🏻 Test: [Pytest](test/pytest/test_rearrange_string.py) [Unittest](test/unittest/test_rearrange_string_unit.py)

<br><br>

## Highest Revenue

you are the manager of a popular e-commerce store You have been tasked to find the product that generates 
the most revenue to the store. you asked one of your employees to write a function that takes in your historical 
transactional data and returns the product that has generated the most revenue. however you notice that the function 
has some issues and you must debug the code. 

The input of the function is a string that contains comma separated data, in which each row represents a 
sale of a particular product and consist in two values: product_id, price_of_product 

Input: '111, 5
111, 5
111, 5 
222, 3
333, 6
333, 6'

Output: 111

Note: the function should return a integer
if a product_id has different prices, then the function should return -1
if the highest revenue is <= 0, then the function should return -1

👩🏻‍💻[Solution](src/highest_revenue.py)
<br>
🕵🏻 Test: [Pytest](test/pytest/test_highest_revenue.py) [Unittest](test/unittest/test_highest_revenue_unit.py)