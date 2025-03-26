bilNumber = int(input("Input number: "))
if bilNumber % 3 == 0:
    print(bilNumber, "is divided by 3 and 4")
elif bilNumber % 4 == 0:
    print(bilNumber, "is divided by 4")
else:
    print(bilNumber, "isn't divided by 3 and 4")
