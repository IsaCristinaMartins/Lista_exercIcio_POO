class Funcionario:
    def __init__(self, nome, salario_base, categoria):
        self.nome = nome
        self.salario_base = salario_base
        self.categoria = categoria

    def calcular_salario(self):
        if self.categoria == "Desenvolvedor":
            if self.salario_base > 3000:
                return self.salario_base * 1.20
            else:
                return self.salario_base * 1.10
        elif self.categoria in ["Tester", "DBA"]:
            if self.salario_base > 3000:
                return self.salario_base * 1.20
            else:
                return self.salario_base * 1.15
        else:
            return self.salario_base


funcionario1 = Funcionario("João", 2500, "Desenvolvedor")
print(f"{funcionario1.nome}: Salário = R${funcionario1.calcular_salario()}")