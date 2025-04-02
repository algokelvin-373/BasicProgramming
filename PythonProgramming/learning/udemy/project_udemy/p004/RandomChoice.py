import random

list_people = ["Andri", "Candra", "Sasha", "Dahlia", "Donny"]

# Using random for index list_people
random_index = random.randint(0, len(list_people) - 1)
print(f"Result 1: {list_people[random_index]}")

# Using random choice
result_random = random.choice(list_people)
print(f"Result 2: {result_random}")