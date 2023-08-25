'''''
Classe Conta de Investimento: Faça uma classe contaInvestimento que 
seja semelhante a classe contaBancaria, com a diferença de que 
se adicione um atributo taxaJuros. Forneça um construtor que configure 
tanto o saldo inicial como a taxa de juros. Forneça um método adicioneJuros
(sem parâmetro explícito) que adicione juros à conta. Escreva um programa que 
construa uma poupança com um saldo inicial de R$1000,00 e uma taxa de juros de 
10%. Depois aplique o método adicioneJuros() cinco vezes e imprime o saldo resultante.
'''

class ContaInvestimento:
    def __init__ (self, jurosCompostos, saldoInicial, saldoFinal, saldo, deposito, retirada):
        self.jurosCompostos = jurosCompostos
        self.saldoInicial = saldoInicial
        self.saldoFinal = saldoFinal
        self.saldo = saldo
        self.deposito = deposito
        self.retirada = retirada
    
    def adicioneJuros(self ):
        self.saldo = self.saldo + (self.saldo * 0.1)
        return self.saldo
    
    def extrato(self):
        return self.saldo
    

class ContaBancaria:
    def __init__ (self, saldo, deposito, retirada):
        self.saldo = saldo
        self.deposito = deposito
        self.retirada = retirada

conta1 = ContaInvestimento(0.1, 1000, 0, 1000, 0, 0)

conta1.adicioneJuros()
conta1.adicioneJuros()
conta1.adicioneJuros()
conta1.adicioneJuros()
conta1.adicioneJuros()
print(f'{conta1.extrato()}, isso é oq ue tem na sua conta de investimentos')