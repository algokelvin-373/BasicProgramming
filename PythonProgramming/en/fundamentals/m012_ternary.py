numberStr = input("Input number: ")
numberInt = int(numberStr)

print('Ternary Operator')
result1 = "positive" if numberInt > 0 else "negative"
print(result1)

print()

print('Ternary Tuple')
result2 = ('negative', 'positive')[numberInt > 0]
print(result2)

print('Done')