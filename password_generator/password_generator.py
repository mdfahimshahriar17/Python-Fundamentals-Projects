import random
capital_letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letters.extend(capital_letters)
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?: "))
nr_symbols = int(input("How many symbols would you like?: "))
nr_numbers = int(input("How many numbers would you like?: "))

#Easy Level
password = ""
for char in range(1, nr_letters+1):
    random_char = random.choice(letters)
    password = password + random_char

for char in range(1, nr_symbols+1):
    password += random.choice(symbols)

for char in range(0, nr_numbers):
    password += random.choice(numbers)

print(f"\n\nReslt fom Option 1 : {password}")

#Diffrent way to use append() and shuffel()
password_list = []
for char in range(1, nr_letters+1):
    password_list.append(random.choice(letters))

for char in range(1, nr_symbols+1):
    password_list += random.choice(symbols)

for char in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

print(f"\n\nResult fomr option 2: {password_list}")

password_in_string = ""
for char in password_list:
    password_in_string+=char

print(f"\n\nResult fomr option 3: {password_in_string}\n\n")
