dictionary_data = {
    "Fruits": "Apple, Banana, Orange",
    "Animals": "Goat, Cow, Buffalo",
    "Code": "Java, Kotlin, Python"
}

print(f"Dictionary Fruits: {dictionary_data['Fruits']}")
print(f"Dictionary Animals: {dictionary_data['Animals']}")
print(f"Dictionary Code: {dictionary_data['Code']}")
print(f"All Dictionary 1:\n{dictionary_data}")

# Add New Dictionary
dictionary_data["Numbers"] = "One, Two, Three"
print(f"Dictionary Numbers: {dictionary_data['Numbers']}")
print(f"All Dictionary 2:\n{dictionary_data}")

#Edit Data Dictionary
dictionary_data["Fruits"] = "Grape, Pineapple, Durian"
print(f"Dictionary Fruits Now: {dictionary_data['Fruits']}")
print(f"All Dictionary 3:\n{dictionary_data}")

#Loop Dictionary
print('Loop Dictionary:')
for key in dictionary_data:
    print(f"Data dictionary {key}: {dictionary_data[key]}")

# Make Empty Data Dictionary
dictionary_data = {}
if len(dictionary_data) == 0:
    print('Data Dictionary Now Empty')
