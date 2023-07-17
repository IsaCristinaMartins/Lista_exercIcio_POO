# Classe Pessoa: Crie uma classe que modele uma pessoa:
#   Atributos: nome, idade, peso e altura
#   Métodos: Envelhercer, engordar, emagrecer, crescer. 
# Obs: Por padrão, a cada ano que nossa pessoa envelhece, 
# sendo a idade dela menor que 21 anos, ela deve crescer 0,5 cm.

class Pessoa:
    def __init__(self, nome, idade, peso, altura):
        self.nome = nome
        self.idade = idade
        self.peso = peso
        self.altura = altura
    
    def envelhecer(self, novaaltura, novaidade):
        novaidade = self.idade +1
        if (novaidade <=21):
            novaaltura = self.altura + (0.5 * (self.idade))
        return novaidade, novaaltura
    
    def engordar(self,sobrepeso):
        self.peso = self.peso + sobrepeso
        return self.peso
    
    def emagrecer(self, subpeso):
        self.peso = self.peso - subpeso
        return self.peso
    
    def crescer(self):
        self.altura = self.altura +1
        return self.altura
    
    
    
i = Pessoa ('Isabel', 20, 85, 1.63)
i.engordar(3)
print (i.peso)

       