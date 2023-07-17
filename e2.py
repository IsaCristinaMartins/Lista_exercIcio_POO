# Classe Quadrado: Crie uma classe que modele um quadrado:
#    Atributos: Tamanho do lado
#    Métodos: Mudar valor do Lado, Retornar valor do Lado e calcular Área;

class Quadrado:
    def __init__(self, lado):
        self.lado = lado
     
    def mudarValorLado(self, novoValorLado):
       self.lado = novoValorLado

    def retornarValor(self):
        print(f'Essa é o valor do lado: {self.lado}')
        return self.lado
    
    def calcularArea(self):
        aux = self.lado ** 2
        return aux

quadrado1 = Quadrado(12)

print (quadrado1.calcularArea)
    
r = Quadrado(6)
q = Quadrado(4)
q.mudarValorLado(2)
    
r= Quadrado(6)
print(r.calcularArea())

i = Quadrado
i.mudarValorLado(15)
