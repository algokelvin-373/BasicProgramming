print('Welcome to the rollercoaster')
height = int(input('Input your height (cm): '))
age = int(input('Input your age: '))

if height > 120:
    print('You can ride the rollercoaster')
    bill = 0
    if age <= 12:
        bill += 5
        print('Child Pay $5')
    elif age <= 18:
        bill += 7
        print('Youth Pay $7')
    else:
        bill += 12
        print('Adult Pay $12')

    is_take_photo = input('Do you want take photos (Pay $3)? (y/n): ')
    if is_take_photo == 'y':
        bill += 3

    print(f"Total bill: {bill}")
else:
    print('Sorry you have to grow taller before you can ride')