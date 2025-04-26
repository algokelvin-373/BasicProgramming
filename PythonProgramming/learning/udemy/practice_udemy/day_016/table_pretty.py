from prettytable import PrettyTable

table = PrettyTable()
table.add_column('ID', [1, 2, 3])
table.add_column('Character', ['Naruto Uzumaki', 'Sasuke Uchiha', 'Sakura Haruno'])

print(table)