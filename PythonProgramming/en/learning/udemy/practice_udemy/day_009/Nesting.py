nesting_data = ["Python", "Dart", ["Java", "Kotlin"]]
print(nesting_data[0])
print(nesting_data[1])
print(nesting_data[2])
print(nesting_data[2][0])
print(nesting_data[2][1])

# Nesting for Dictionary
nesting_dictionary = {
    "Fruits": ["Apple", "Banana", "Orange"],
    "Animals": ["Goat", "Cow", "Buffalo"],
    "Code": ["Java", "Kotlin", "Python"]
}

print(f"Nesting Fruits: {nesting_dictionary['Fruits']}")
print(f"Nesting Fruits: {nesting_dictionary['Fruits'][0]}")
print(f"Nesting Fruits: {nesting_dictionary['Fruits'][1]}")
print(f"Nesting Fruits: {nesting_dictionary['Fruits'][2]}")

print(f"Nesting Animals: {nesting_dictionary['Animals']}")
print(f"Nesting Animals: {nesting_dictionary['Animals'][0]}")
print(f"Nesting Animals: {nesting_dictionary['Animals'][1]}")
print(f"Nesting Animals: {nesting_dictionary['Animals'][2]}")

print(f"Nesting Code: {nesting_dictionary['Code']}")
print(f"Nesting Code: {nesting_dictionary['Code'][0]}")
print(f"Nesting Code: {nesting_dictionary['Code'][1]}")
print(f"Nesting Code: {nesting_dictionary['Code'][2]}")

# Nesting Dictionary like JSON
nesting_json = {
    "Java": {
        "Implementation": ["Android", "Web Springboot"],
        "Count": 2
    },
    "Dart": {
        "Implementation": ["Flutter", "Android", "iOS"],
        "Count": 3
    }
}
print(nesting_json)