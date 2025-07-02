def full_name(first_name, last_name):
    format_first_name = first_name.title()
    format_last_name = last_name.title()
    return f"{format_first_name} {format_last_name}"

print(full_name('kelvin', 'tandrio'))