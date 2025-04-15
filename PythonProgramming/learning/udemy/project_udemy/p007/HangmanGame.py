import random

word_list = ["apple", "banana", "orange"]

choose_word = random.choice(word_list)
print('Choose word: '+ choose_word)

placeholder = ""
for position in range(len(choose_word)):
    placeholder += "_"
print(placeholder)

lives = 3
game_over = False
correct_letters = []
while not game_over:
    guess = input('Guess a letter: ').lower()

    display = ""
    for letter in choose_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    print(display)

    if guess not in choose_word:
        lives -= 1
        print(f'Lives: {lives}')
        if lives == 0:
            game_over = True
            print('You lose')

    if "_" not in display:
        game_over = True
        print("You win")