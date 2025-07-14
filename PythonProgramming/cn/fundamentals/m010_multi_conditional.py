numberStr = input("Input number: ")

numberInt = int(numberStr)
if numberInt > 0:
    print('正数')
elif numberInt == 0:
    print('零')
else:
    print('负数')

print('完成')