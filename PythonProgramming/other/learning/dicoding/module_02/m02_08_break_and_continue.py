print("***** BREAK *****")
dataList01 = [2, 4, 21, 16, 24, 22, 87]
for x in range(len(dataList01)):
    if dataList01[x] % 3 == 0 and dataList01[x] % 4 == 0:
        print("\n", dataList01[x], " is divided by 3 and 4")
        break
    print(dataList01[x], " ", end='')

print("***** CONTINUE *****")
dataList02 = [2, -3, 4, 1, -9, 6, -5]
for x in range(len(dataList02)):
    if dataList02[x] < 0:
        dataList02[x] = abs(dataList02[x])
        print(dataList02[x], " ", end='')
        continue
    print(dataList02[x], " ", end='')
