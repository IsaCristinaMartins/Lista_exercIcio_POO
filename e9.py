'''''
Classe Ponto e Retangulo: Faça um programa completo utilizando funções e classes que:

Possua uma classe chamada Ponto, com os atributos x e y.
Possua uma classe chamada Retangulo, com os atributos largura e altura.
Possua uma função para imprimir os valores da classe Ponto
Possua uma função para encontrar o centro de um Retângulo.
Você deve criar alguns objetos da classe Retangulo.
Cada objeto deve ter um vértice de partida, por exemplo, 
    o vértice inferior esquerdo do retângulo, 
    que deve ser um objeto da classe Ponto.
A função para encontrar o centro do retângulo deve retornar 
    o valor para um objeto do tipo ponto que indique os valores de 
    x e y para o centro do objeto.
O valor do centro do objeto deve ser mostrado na tela
Crie um menu para alterar os valores do retângulo e imprimir o centro deste retângulo.
'''


class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def imprimir(self):
        print(f'{self.x}, {self.y}')

class Retangulo:
    def __init__ (self, largura, altura):
        self.largura = largura
        self.altura = altura 

    def area(self, largura, altura):
        a = largura * altura
        return a
       

    def ponto_central(self, meiolargura, meioaltura):
        meiolargura = self.largura/2
        meioaltura = self.altura/2
        return meioaltura, meiolargura
    
while True:
    print(f'Vamos fazer um retângulo??')
    print(f'Escolha os valores de altura e largura do retângulo')
    alt = int(input(f'Altura:  '))
    larg = int(input(f'Largura:  '))
    print("Escreva \'esc\' para sair")
    opt = input(">>")

    if opt == "esc":
        break

ret = Retangulo(larg, alt)




