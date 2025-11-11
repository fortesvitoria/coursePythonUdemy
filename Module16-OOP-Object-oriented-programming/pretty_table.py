from prettytable import PrettyTable
table = PrettyTable()

table.field_names = ["Nome", "Sobrenome", "Ano Nascimento"]
table.add_row(["Vitoria", "Fortes", 1991])
table.add_row(["Michelle", "Viscardi", 1990])
table.add_rows(
    [
        ["Eduardo", "Riguera", 1984],
        ["Lucas", "Mankowski", 1990]
    ]
)

table.add_column("Cidade", ["POA", "POA", "RJ", "Viamao"])

table.align["Nome"] = "l"
table.align["Sobrenome"] = "l"

print(table)