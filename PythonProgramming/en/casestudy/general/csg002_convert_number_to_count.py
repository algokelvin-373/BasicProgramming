def unit(number):
    match number:
        case 0: return ""
        case 1: return "Satu"
        case 2: return "Dua"
        case 3: return "Tiga"
        case 4: return "Empat"
        case 5: return "Lima"
        case 6: return "Enam"
        case 7: return "Tujuh"
        case 8: return "Delapan"
        case 9: return "Sembilan"

def unit100(number):
    div_100 = int(number / 100)
    if div_100 == 1:
        return ' Seratus '
    elif 2 <= div_100 <= 9:
        return unit(div_100) + " Ratus "
    else:
        return ""

def unit10(number):
    div_10 = int(number / 10)
    if div_10 == 1:
        return ' Sepuluh '
    elif 2 <= div_10 <= 9:
        return unit(div_10) + " Puluh "
    else:
        return ""

numbers = int(input('Input number: '))

num_count = ''

num_count += unit100(numbers)

mod_100 = numbers % 100
num_count += unit10(mod_100)

mod_10 = mod_100 % 10
num_count += unit(mod_10)

print(num_count)