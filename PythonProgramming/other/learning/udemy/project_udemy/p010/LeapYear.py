def is_leap_year(year):
    if year % 4 == 0:
        if year % 400 == 0 or year % 100 != 0:
            return True
        else:
            return False
    else:
        return False

print(is_leap_year(1700))
print(is_leap_year(1800))
print(is_leap_year(2020))
print(is_leap_year(2100))