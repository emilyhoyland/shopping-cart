# shopping_cart.py

# from GitHub Setup:

products = [
    {"id":1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id":2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id":3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id":4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id":5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id":6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id":7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id":8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id":9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id":10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id":11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id":12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id":13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id":14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id":15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id":16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id":17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id":18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id":19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id":20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
] # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017


def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.

    Param: my_price (int or float) like 4000.444444

    Example: to_usd(4000.444444)

    Returns: $4,000.44
    """
    return f"${my_price:,.2f}" #> $12,000.71

    #print(products)


# TODO: write some Python code here to produce the desired output

# how to capture product identifiers and store them for use later
# take captured identifiers and use them to perform calculations
    #look up items price, assemble a runnning total, add tax 


#CHECKPOINT 1: CAPTURING USER INPUTS

# Ask for user input and information capture 
# parameter of input function is a textual message to be passed to user

# Source (for input): Class + Screencast (copied from personal note-taking in Colab )
selected_products = [] # place to store inputs in list #okay to contain duplicates 
print(type(selected_products))
total_price = 0 # has to be defined before loop in order to add prices 

while True:
    # store results of input in variable: 
    selected_id = input("Please select a product identifier (1-20):") # waits for input before next iteration
    # ID is the value we want to compare with our list attributes
    print(selected_id) # produces a string
    #print(type(selected_id)) # confirm data type we are working with
    if selected_id == "DONE": # ADD: CONVERT TO LOWERCASE
        break #stops generating the request
    #CHECKPOINT 2: LOOK-UP PRODUCTS
    else:
        # do a filtering operation
        # for each product in list
        # if selected_id equal to product's "id" attribute
 
        selected_products = [p for p in products if str(p["id"]) == str (selected_id)]
        selected_products = selected_products[0]
        total_price = total_price + selected_products["price"]   # accumulate value of total price
        print("SELECTED PRODUCT: " + selected_products["name"] + " " + str(selected_products["price"]))
        #TO-DO: Convert to USD
        
        #Original work REMOVED 6/28 due to errors with recognizing integers
        #for x in products:
         # if str(x["id"]) == str(selected_id): #convert to same datatype that allows them to be compared (string)
            #print(x["name"] + " " + str(x["price"])) # Added price, had to convert number to string (logic from screencast)
            #ADD: PRICE in USD
            # total_price = total_price + str(selected_id["price"])
            # selected_products.append(x)
        

#INFO DISPLAY/OUTPUTS
#CHECKPOINT 3: PRINTING THE RECEIPT
print("You have purchased", len(selected_products), "products...") #count number of inputs #COMMENT OUT
print("now time to generate a receipt")


print("TOTAL PRICE: " + str(total_price)) # ADD: FORMAT AS USD





#RECEIPT INCLUDES:
#A grocery store name of your choice
#A grocery store phone number and/or website URL and/or address of choice
#The date and time of the beginning of the checkout process, formatted in a human-friendly way (e.g. 2020-02-07 03:54 PM)
#The name and price of each shopping cart item, price being formatted as US dollars and cents (e.g. $3.50, etc.)
#The total cost of all shopping cart items (i.e. the "subtotal"), formatted as US dollars and cents (e.g. $19.47), calculated as the sum of their prices
#The amount of tax owed (e.g. $1.70), calculated by multiplying the total cost by a New York City sales tax rate of 8.75% (for the purposes of this project, groceries are not exempt from sales tax)
#The total amount owed, formatted as US dollars and cents (e.g. $21.17), calculated by adding together the amount of tax owed plus the total cost of all shopping cart items
#A friendly message thanking the customer and/or encouraging the customer to shop again



