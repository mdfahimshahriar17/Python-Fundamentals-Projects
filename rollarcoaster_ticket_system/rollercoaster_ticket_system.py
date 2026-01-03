print("Welcome to the rollercoaster!")
height = int(input("What is your height in CM?"))

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age: "))
    if age <= 12:
        ticket_price = 5

    elif age > 12 and age <= 18:
        ticket_price = 7
    
    elif age >= 45 and age <=55:
        print("Everything is going to be ok. Have a free rides on us!")
       
    else:
        ticket_price = 12

    print(f"The ticket price is ${ticket_price}")
    
    photo = input("Do you want photo? $3 press y for photo press n for skip: ")
    if photo.lower() == 'y':
        ticket_price = ticket_price + 3

    print(f"Your total bill is ${ticket_price}")


else:
    print("You are not eligibale for the ride")