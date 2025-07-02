# FizzBuzz
# You are going to write a program that automatically prints the solution to the FizzBuzz game. These are the rules of the FizzBuzz game:
# Your program should print each number from 1 to 100 in turn and include number 100.
# But when the number is divisible by 3 then instead of printing the number it should print "Fizz".
# When the number is divisible by 5, then instead of printing the number it should print "Buzz".`
# And if the number is divisible by both 3 and 5 e.g. 15 then instead of the number it should print "FizzBuzz"

for number in range(1, 101):
    logic1 = number % 3 == 0
    logic2 = number % 5 == 0
    if logic1 and logic2:
        print('FizzBuzz')
    elif logic1:
        print('Fizz')
    elif logic2:
        print('Buzz')
    else:
        print(number)