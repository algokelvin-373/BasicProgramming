import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

data = int(input(f"(0) Rock or (1) Paper or (2) Scissors? "))
random_data = random.randint(0, 2)

print('You Choose:')
if data == 0:
    print(rock)
elif data == 1:
    print(paper)
elif data == 2:
    print(scissors)

print('Computer Choose:')
if random_data == 0:
    print(rock)
elif random_data == 1:
    print(paper)
elif random_data == 2:
    print(scissors)

if data == random_data:
    print('Draw')
else:
    if data == 0:
        if random_data == 2:
            print('You Win')
        else:
            print('You Lose')
    elif data == 1:
        if random_data == 0:
            print('You Win')
        else:
            print('You Lose')
    elif data == 2:
        if random_data == 1:
            print('You Win')
        else:
            print('You Lose')
    else:
        print('You input is Invalid. You Lose!!')