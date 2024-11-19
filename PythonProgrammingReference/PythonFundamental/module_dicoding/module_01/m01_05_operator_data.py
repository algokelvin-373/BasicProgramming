print("***** Tuple *****")
dataTuple = (23, 'Kelvin', 17.5, 2 + 3j)
print("dataTuple[0] = ", dataTuple[0])
print("dataTuple[1:3] = ", dataTuple[1:3])
# dataTuple[2] = 0 --> Tuple cannot change item

print("\n***** Set *****")
dataSet = {1, 2, 3, 2, 4, 5, 1, 6}  # Set can avoid duplicate data
print("dataSet = ", dataSet)

print("\n***** Dictionary *****")
dataDictionary = {1: 'Kelvin', 'Programming': 'Python'}
print("Type dataDictionary = ", type(dataDictionary))
print("The value of dataDictionary[1] = ", dataDictionary[1])
print("The value of dataDictionary['Programming'] = ", dataDictionary['Programming'])
