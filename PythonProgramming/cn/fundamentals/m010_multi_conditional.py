numberStr = input("Input number: ")

numberInt = int(numberStr)
if numberInt > 0:
    print('Positive')
elif numberInt == 0:
    print('Zero')
else:
    print('Negative')

print('Done')