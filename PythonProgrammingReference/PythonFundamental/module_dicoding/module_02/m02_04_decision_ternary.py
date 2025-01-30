print("***** Ternary Model 1 *****")
bil1 = int(input("Input number = "))
print(bil1, "is ", "negative" if (bil1 < 0) else "positive")

print("\n***** Ternary Model 2 *****")
bil2 = int(input("Input number = "))
print(bil2, "is ", ("odd", "even")[bil2 % 2 == 0])

print("\n***** Short Ternary *****")
output = None
msg = output or "No data returned"  # This function to avoid get error when this value is null data
print(msg)
