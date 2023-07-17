'''''
Classe Macaco: Desenvolva uma classe Macaco,que possua os 
atributos nome e bucho (estomago) e pelo menos os métodos comer(),
 verBucho() e digerir(). Faça um programa ou teste interativamente,
   criando pelo menos dois macacos, alimentando-os com pelo menos 3 alimentos 
   diferentes e verificando o conteúdo do estomago a cada refeição. 
   Experimente fazer com que um macaco coma o outro. 
   É possível criar um macaco canibal?
'''
class Macaco:
    def __init__(self, nome, bucho, comida):
        self.nome = nome
        self.bucho = bucho
        self.comida = comida

    def comer(self, alimento):
        self.comida = self.comida + alimento
        return self.comida
    
    def ver_estomago(self, alimento):
        self.bucho = self.bucho + alimento
        if self.bucho>=100:
            print(f'Macaco cheio')
        
        print(f'Macaco ainda pode comer mais')
        return self.bucho
        
    def digerir(self, digestao):
        self.bucho = self.bucho - digestao
        if self.bucho <=5:
            print(f'Digestão completamente concluida')
        elif self.bucho>=6 and self.bucho<=80:
            print(f'Digestão em andamento')
        print(f'Iniciando digestão')
        return self.bucho 
    
gorila1 = Macaco('Gorila', 0, 10)
mico = Macaco('Mico', 0, 5)

gorila1.comer(50)
mico.comer(60)

print(gorila1.ver_estomago(50))
print(mico.ver_estomago(60))

print(gorila1.ver_estomago(50))