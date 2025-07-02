print('Welcome to the rollercoaster')
height = int(input('Input your height (cm): '))
age = int(input('Input your age: '))

if height > 120:
    print('You can ride the rollercoaster')
    if age <= 12:
        print('Please Pay $5')
    elif age <= 18:
        print('Please Pay $7')
    else:
        print('Please Pay $12')
else:
    print('Sorry you have to grow taller before you can ride')