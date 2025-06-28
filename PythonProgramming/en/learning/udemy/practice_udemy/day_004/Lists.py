state_of_indonesian = [
    "Jakarta",
    "Semarang",
    "Surabaya",
    "Palembang",
    "abc",
    "Lampung",
    "def",
    "Manado",
    "Bali"
]

print(f"List Before: {state_of_indonesian}")

state_of_indonesian[4] = "Palembang" # Change for index 4
state_of_indonesian[6] = "Pontianak" # Change for index 6
print(f"List After 1: {state_of_indonesian}")

state_of_indonesian.append("Makasar") # Push one data
print(f"List After 2: {state_of_indonesian}")

list_data = ["Ternate, Merauke"]
state_of_indonesian.extend(list_data) # Push list - more than one data
print(f"List After 3: {state_of_indonesian}")