import prettytable
from prettytable import PrettyTable
#gan table bang cai bang hien taij
table = PrettyTable()
table.add_column("pokemon name", ["pikachu","turle","hoise"])
table.add_column("type",["electric","fire","water"])

table.align = 'l'
print(table)