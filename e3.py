# Classe Retangulo: Crie uma classe que modele um retangulo:

# Atributos: LadoA, LadoB (ou Comprimento e Largura, ou Base e Altura, a escolher)
# Métodos: Mudar valor dos lados, Retornar valor dos lados, calcular Área e calcular Perímetro;
# Crie um programa que utilize esta classe. Ele deve pedir ao usuário que informe as
#    medidades de um local. Depois, deve criar um objeto com as medidas e calcular a 
#    quantidade de pisos e de rodapés necessárias para o local.

class Retangulo:
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura =  largura
    
    def mudarValor(self, nvcomprimento, nvlargura):
        self.comprimento = nvcomprimento
        self.largura = nvlargura
    
    def returnarValorLados(self):
        print(f'O valor do comprimento é {self.comprimento} e o valor da largura é {self.largura}')

    def calcularArea(self):
        return self.comprimento * self.largura

    def calcularPerimetro(self):
        return (self.comprimento * 2) + (self.largura * 2)
            
    

larg = int(input("Digite aqui a largura:  "))
compr = int(input("Digite aqui o comprimento:  "))

ad = Retangulo(larg, compr)

x = ad.calcularArea() # x = self.comprimento * self.largura
print(x)
#print(ad.calcularArea())   # == print(x)