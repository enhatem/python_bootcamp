#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

total_with_tip = total_bill * (1 + tip / 100)
bill_per_person = total_with_tip / people

rounded_bill_per_person = round(bill_per_person, 2)
rounded_bill_per_person = "{:.2f}".format(rounded_bill_per_person) # formatting value

print(f"Each person should pay: ${rounded_bill_per_person}")
