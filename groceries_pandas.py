# groceries.py

import operator


import pandas

csv_filepath = "products.csv"
df = pandas.read_csv(csv_filepath)
print(type(df)) #> <class 'pandas.core.frame.DataFrame'>

# todo: assemble a list of dictionaries

# APPROACH A

#products = []
#
#for row in _____________: # how to loop through each row in a dataframe
#    products.append({}) # how to convert each row to a dictionary


# APPROACH B

products = df.to_dict("records")




def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71



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
