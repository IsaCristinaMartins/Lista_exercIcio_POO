'''''
Classe carro: Implemente uma classe chamada Carro com as seguintes propriedades:

Um veículo tem um certo consumo de combustível (medidos em km / litro) e uma certa quantidade de combustível no tanque.
O consumo é especificado no construtor e o nível de combustível inicial é 0.
Forneça um método andar( ) que simule o ato de dirigir o veículo por uma certa distância, reduzindo 
o nível de combustível no tanque de gasolina.
Forneça um método quantiddeTanque( ), que retorna o nível atual de combustível.
Forneça um método adicionarGasolina( ), para abastecer o tanque. Exemplo de uso:

'''

class Carro:
    def __init__ (self, consumo, tanque):        
        self.q_consumo = consumo
        self.tanque = tanque

    def andar (self, quilometro):
        self.tanque = self.tanque - quilometro  
        return self.tanque

    def quantidadeTanque(self):
        return self.tanque        
    
    def adicionarGasolina(self, gasolina):
        self.tanque = self.tanque + gasolina
        return self.tanque
    
    def qConsumo(self, quilometro, gasolina):
        self.consumo = quilometro / gasolina 
        return self.consumo


carro1 = Carro(10, 4, 0)

carro1.adicionarGasolina(50)
print(carro1.quantidadeTanque())
print(f'Agora o carro vai andar 10km')
carro1.andar(10)
print(f'Seu carro agora tem {carro1.quantidadeTanque()} litros de gasolina')