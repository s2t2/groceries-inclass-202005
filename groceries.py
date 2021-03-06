# groceries.py

import operator

import csv

# todo: assemble a new products variable by reading from CSV file

products = []

csv_filepath = "products.csv" # a relative filepath
with open(csv_filepath, "r") as csv_file: # "r" means "open the file for reading"
    reader = csv.DictReader(csv_file) # assuming your CSV has headers
    for row in reader:
        # print(type(row)) #> <class 'collections.OrderedDict'>
        #print(type(row), row["id"], row["name"], row["price"])
        #products.append(row) #> gives us price values as string
        row["price"] = float(row["price"]) # change the price from string to float
        products.append(row)

#products = [
#    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
#    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
#    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
#    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
#    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
#    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
#    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
#    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
#    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
#    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
#    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
#    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
#    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
#    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
#    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
#    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
#    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
#    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
#    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
#    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
#] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

#{
#    "id":1,
#    "name": "Chocolate Sandwich Cookies",
#    "department": "snacks",
#    "aisle": "cookies cakes",
#    "price": 3.50
#}
#example_department_name = "snacks"
#
#matching_products = [x for x in products if x["department"] == example_department_name]
#
#print(type(matching_products)) #> list
#print(matching_products)






#print(type(products)) #> list

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71


print(to_usd(1000000))

# PART 1 (PRODUCTS)
# --------------
# THERE ARE 20 PRODUCTS:
# --------------
#  + All-Seasons Salt ($4.99)
#  + Chocolate Fudge Layer Cake ($18.50)
#  + Chocolate Sandwich Cookies ($3.50)
#  + Cut Russet Potatoes Steam N' Mash ($4.25)
#  + Dry Nose Oil ($21.99)
#  + Fresh Scent Dishwasher Cleaner ($4.99)
#  + Gluten Free Quinoa Three Cheese & Mushroom Blend ($3.99)
#  + Green Chile Anytime Sauce ($7.99)
#  + Light Strawberry Blueberry Yogurt ($6.50)
#  + Mint Chocolate Flavored Syrup ($4.50)
#  + Overnight Diapers Size 6 ($25.50)
#  + Peach Mango Juice ($1.99)
#  + Pizza For One Suprema Frozen Pizza ($12.50)
#  + Pomegranate Cranberry & Aloe Vera Enrich Drink ($4.25)
#  + Pure Coconut Water With Orange ($3.50)
#  + Rendered Duck Fat ($9.99)
#  + Robust Golden Unsweetened Oolong Tea ($2.49)
#  + Saline Nasal Mist ($16.00)
#  + Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce ($6.99)
#  + Sparkling Orange Juice & Prickly Pear Beverage ($2.99)

# COUNT THE PRODUCTS

print("------------------")
print("NUMBER OF PRODUCTS:", len(products))
print("------------------")

# SORT THE PRODUCTS

sorted_products = sorted(products, key=operator.itemgetter("name"))

# LOOP THROUGH THE PRODUCTS AND PRINT EACH ONE

for x in sorted_products:
    #print("-----")
    #print(type(x))
    #print(x)
    #print("name")
    #print(x["name"])
    # + Cut Russet Potatoes Steam N' Mash ($4.25)
    #print(" + Cut Russet Potatoes Steam N' Mash ($4.25)")
    price_usd = to_usd(x["price"]) # "($4.25)"
    print(f" + {x['name']} ({price_usd})")

# PART 2 (DEPARTMENTS)
#
# --------------
# THERE ARE 10 DEPARTMENTS:
# --------------
#  + Babies (1 product)
#  + Beverages (5 products)
#  + Dairy Eggs (1 product)
#  + Dry Goods Pasta (1 product)
#  + Frozen (4 products)
#  + Household (1 product)
#  + Meat Seafood (1 product)
#  + Pantry (2 products)
#  + Personal Care (2 products)
#  + Snacks (2 products)

departments = []

for x in products:
    if x["department"] not in departments:
        departments.append(x["department"])

print("------------------")
print("NUMBER OF DEPARTMENTS:", len(departments))
print("------------------")

departments = sorted(departments)

for dept_name in departments:
    matching_products = [x for x in products if x["department"] == dept_name]
    matching_products_count = len(matching_products)
    print(f"  + {dept_name.title()} -- {matching_products_count} product(s)")
