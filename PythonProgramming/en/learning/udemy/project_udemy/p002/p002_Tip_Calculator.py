# Project Day 2 - Tip Calculator

print("Welcome to Tip Calculator")
bill = input("What was the total bill? $")
percentage = input("What percentage tip would you like to give? 10 / 12 / 15? ")
people = input("How many people to split the bill? ")

bill_float = float(bill)
percentage_float = int(percentage) / 100
people_int = int(people)

total_tip = bill_float * percentage_float
total_bill = bill_float + total_tip
bill_per_person = total_bill / people_int

print("Each person should pay: $", round(bill_per_person, 2))
