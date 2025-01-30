bilNumber = int(input("Input number: "))
if bilNumber % 3 == 0 and bilNumber % 4 == 0:
    print(bilNumber, "is divided by 3 and 4")
elif bilNumber % 3 == 0 or bilNumber % 4 == 0:
    print(bilNumber, "is divided by 3 or 4")
else:
    print(bilNumber, "isn't divided by 3 and 4")
