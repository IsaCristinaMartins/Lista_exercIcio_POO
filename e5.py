#Classe Conta Corrente: Crie uma classe para implementar uma conta corrente.
# A classe deve possuir os seguintes atributos: número da conta, 
# nome do correntista e saldo. Os métodos são os seguintes: alterarNome, 
# depósito e saque; No construtor, saldo é opcional, com valor default zero 
# e os demais atributos são obrigatór

class ContaCorrente:
    def __init__(self, numero_da_conta, nome_correntista, saldo):
        self.numero_da_conta = numero_da_conta
        self.nome_correntista = nome_correntista
        self.saldo = saldo

    def teste(self, numero_da_conta):
        if numero_da_conta == self.numero_da_conta:
            print (f"Número da conta certo, favor continuar a operação")
            return True
        
        print (f"número da conta errado, favor digitar o número certo")
        return False

    def alterar_nome (self, novonome, numero_da_conta):
        validacao_conta = self.teste(numero_da_conta)
        if validacao_conta == True:
            self.nome_correntista = novonome
        return self.nome_correntista

    def deposito(self, depositovalor, numero_da_conta):
        validacao_conta = self.teste(numero_da_conta)
        if validacao_conta == True:
           self.saldo = self.saldo + depositovalor
        return depositovalor, self.saldo

    def saque(self, retirada, numero_da_conta):
        validacao_conta = self.teste(numero_da_conta)
        if validacao_conta == True:
            self.saldo = self.saldo - retirada
        return retirada, self.saldo  
    
         
    
i = ContaCorrente(2654, "Isabel", 2000)   

pedro = ContaCorrente(1234, "Pedro Freire", 15000)


print(pedro.deposito(2000, 3211))

   

    
    
  

