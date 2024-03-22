"""
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
"""


def highest_revenue_item(data):
    count_dict = {}
    price_dict = {}

    row_data = data.split("\n")  # Corrected to split by newline character
    for row in row_data:
        txn = row.split(",")
        product_id = txn[0]  # Corrected index for product_id
        price = int(txn[1])  # Corrected to convert price to integer

        if product_id in count_dict:
            if price_dict[product_id] != price:  # Check if prices are different
                return -1
            count_dict[product_id] += 1
        else:
            count_dict[product_id] = 1
            price_dict[product_id] = price

    most_common_item = None
    most_revenue = 0

    for product in count_dict:
        product_revenue = price_dict[product] * count_dict[product]
        if product_revenue > most_revenue:
            most_revenue = product_revenue
            most_common_item = product

    if most_revenue <= 0:  # Check if highest revenue is <= 0
        return -1

    return int(
        most_common_item
    )  # Return the product_id generating the most revenue as an integer


# Test the function with the provided input
data = """111, 5
111, 5
111, 5
222, 3
333, 6
333, 6"""
output = highest_revenue_item(data)
print(output)
