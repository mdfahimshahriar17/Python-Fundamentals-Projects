print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip_percantage = int(input("How many percantage tip would you like to give? 10, 12, or 15? "))
split_bill_per_person = float(input("How many people to split the bill?"))

bill_for_per_person = ((((bill/100)*tip_percantage)+bill)/split_bill_per_person)
print(tip_percantage)
print(bill)
print(f"Each person should pay: ${bill_for_per_person:.2f}")  