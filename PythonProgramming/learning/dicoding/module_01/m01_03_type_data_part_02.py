print("Basic Type Data -> List")

list01 = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]  # list Integer
print("List = ", list01)
print("Value list01[3] = ", list01[3])
print("Value list01[-1] = ", list01[-1])    # Set from last index
print("Value list01[5:8] = ", list01[5:8])  # Set from index 5 - 7
print("Value list01[:3] = ", list01[:3])    # Set from index 0 - 2
print("Value list01[6:] = ", list01[6:])    # Set from index 6 - last index
print("Value list01[2:6:8] = ", list01[2:9:2])  # Set from index 2 - 9 with step 2 [start:finish:step]

list02 = [1, 3.4, "Python", "Kotlin", 12, 3.4, 2,3]
print("\n")
print("List = ", list02)
list02[1] = "Java"  # Replace into 'Java'
print("List = ", list02)
list02.append(2345)     # Add new data '2345'
print("List = ", list02)
del list02[4]   # Delete item data in index 4
print("List = ", list02)
