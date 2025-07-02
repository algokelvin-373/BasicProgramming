# Function with 1 input
def greet(name):
    print(f'Hello {name}')
    print(f'How do you do, {name}?')

def life_in_weeks(age):
    weeks = (90 - age) * 52
    print(f"You have {weeks} weeks left.")

greet('Kelvin')
greet('Jenny')
life_in_weeks(56)

#Function with more than 1 input
def greet_with_location(name, location):
    print(f'Hello {name}')
    print(f'What is it like in {location}?')

greet_with_location('Kelvin', 'Indonesian')
greet_with_location('Dian', 'US')