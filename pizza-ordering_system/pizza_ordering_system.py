print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pizza_price = 0

if size.lower() == 's':
    pizza_price = 15

elif size.lower() == 'm':
    pizza_price = 20

elif size.lower() == 'l':
    pizza_price = 25

else:
    print("Wrong choice")


if pizza_price > 0:
    pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
    if pepperoni.lower() == 'y':
        pizza_price += 3
    
    cheese = input("Do you want extra cheese? Y or N: ")
    if cheese.lower() == 'y':
        pizza_price = pizza_price + 1

    print(f"Your final bill is ${pizza_price}")