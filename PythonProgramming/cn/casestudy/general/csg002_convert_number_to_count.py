def unit(number):
    if number == 1:
        return "Satu"
    elif number == 2:
        return "Dua"
    elif number == 3:
        return "Tiga"
    elif number == 4:
        return "Empat"
    elif number == 5:
        return "Lima"
    elif number == 6:
        return "Enam"
    elif number == 7:
        return "Tujuh"
    elif number == 8:
        return "Delapan"
    elif number == 9:
        return "Sembilan"

numbers = int(input('Input number: '))

num_count = ''
div_100 = int(numbers / 100)
if div_100 == 1:
    num_count += ' Seratus '
elif 2 <= div_100 <= 9:
    num_count += unit(div_100) + " Ratus "

mod_100 = numbers % 100
div_10 = int(mod_100 / 10)
if div_10 == 1:
    num_count += ' Sepuluh '
elif 2 <= div_10 <= 9:
    num_count += unit(div_10) + " Puluh "

mod_10 = mod_100 % 10
num_count += unit(mod_10)

print(num_count)