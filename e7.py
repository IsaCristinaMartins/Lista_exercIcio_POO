'''''
Classe Bichinho Virtual:Crie uma classe que modele um Tamagushi (Bichinho Eletrônico):

Atributos: Nome, Fome, Saúde e Idade 
b. Métodos: Alterar Nome, Fome, Saúde e Idade; 
Retornar Nome, Fome, Saúde e Idade 
Obs: Existe mais uma informação que devemos levar em
consideração, o Humor do nosso tamagushi, este humor
é uma combinação entre os atributos Fome e Saúde, ou seja, 
um campo calculado, então não devemos criar um atributo para 
armazenar esta informação por que ela pode ser calculada a qualquer momento.
'''

class Tamagushi:
    def __init__ (self, nome, fome, saude, idade):
        self.nome =  nome
        self.fome = fome
        self.saude = saude
        self.idade = idade


    def alterar_nome(self, novonome):
        self.nome = novonome
        return self.nome


    def nutricao(self, comida):
        self.fome = self.fome - (comida)
        if self.fome == 0:
            print (f'O bichinho ta cheio')
        return self.fome


    def vitalidade(self, doenca):
        self.saude = 100
        self.saude = self.saude - doenca
        if self.saude < doenca :
            print(f'Seu bichinho ta dodoi')
        return self.saude


    def ciclo(self, ano):
        self.idade = self.idade + ano
        return self.idade

    def humor(self):
        felicidade = self.fome == 0 and self.saude >=50
        tristeza = self.fome >=50 and self.saude<=49

        if felicidade == True:
            print(f'Seu bichinho ta feliz')
        else:
            print (f'Seu bichinho ta triste')        
        return felicidade, tristeza

mabely_biju = Tamagushi('Mabely Biju', 40, 100, 5) 

print(mabely_biju.nutricao(10))
print(mabely_biju.nutricao(10))
print(mabely_biju.nutricao(10))
print(mabely_biju.nutricao(10))



