'''def factorial(n):
    if n==1:
        return 1 
    return n * factorial(n-1)
n=int(input("Enter a number"))
print(factorial(n))


you are buliding a ceckout system for an online store .
   write a function calculate total the    a list of dictionary , where each 
dictionary represent as item in the shopping cart , each item has 
name:product_name
price:product_price
quantity:purchased_quantity
your function should return the total cost of all the item in the cart , rounded to 2 decimal place
 '''


def calculate_total(cart):
    total = 0
    for item in cart:
        total += item["price"] * item["quantity"]
    return round(total, 2)

# Take user input
cart = []
n = int(input("Enter number of items: "))

for i in range(n):
    print(f"\nItem {i+1}:")
    name = input("Enter product name: ")
    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))
    
    cart.append({"name": name, "price": price, "quantity": quantity})

# Calculate and display total
total_cost = calculate_total(cart)
print("\nTotal cost of your cart:", total_cost)
