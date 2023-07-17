#Classe Bola: Crie uma classe que modele uma bola:
#    Atributos: Cor, circunferência, material
#    Métodos: trocaCor e mostraCor

class Bola:
    def __init__ (self, cor, circunferencia, material): # o __init__ é a função principal de uma classe.
        self.cor = cor
        self.circunferencia = circunferencia
        self.material = material
    
    def trocaCor (self, nova_cor):
        self.cor = nova_cor
    
    def mostraCor(self):
        print (f"A nova cor é {self.cor}")

bola_bel = Bola("azul", 40, "vidro")
bola_bel.mostraCor()

bola_bel.trocaCor("vermelha")

bola_bel.mostraCor()

