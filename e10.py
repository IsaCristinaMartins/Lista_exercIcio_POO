'''''
Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

a>> Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
    tipoCombustivel.
    valorLitro
    quantidadeCombustivel
b>> Possua no mínimo esses métodos:
    abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra
a quantidade de litros que foi colocada no veículo
    abastecerPorLitro( ) – método onde é informado a quantidade em litros
de combustível e mostra o valor a ser pago pelo cliente.
    alterarValor( ) – altera o valor do litro do combustível.
    alterarCombustivel( ) – altera o tipo do combustível.
    alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
    OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.
'''

class BombaCombustivel:
    def __init__ (self, tipo_combustivel=None, valorLitro=None, quantidade_combustivel=None, valor_pago=None, volume_bomba=None):
        self.tipo_combustivel = tipo_combustivel
        self.valorLitro = valorLitro
        self.quantidade_combustivel = quantidade_combustivel 
        self.valor_pago = valor_pago
        self.volume_bomba = volume_bomba
        
    
# método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
    def abastecerPorValor(self):
        if self.valorLitro == None:
            print("o valor do litro esta nulo")
            return
        
        self.quantidade_combustivel = self.valor_pago / self.valorLitro
        return self.quantidade_combustivel
    
# método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
    def abastecerPorLitro(self):
        self.valor_pago = (self.valorLitro) * (self.quantidade_combustivel)
        return float(self.valor_pago)

# altera o valor do litro do combustível.
    def alterarValor(self, novoValorLitro): 
        self.valorLitro = novoValorLitro
        return self.valorLitro

# altera o tipo do combustível.
    def alterarCombustivel(self, outroCombustivel):
        self.tipo_combustivel = outroCombustivel
        return self.tipo_combustivel

# altera a quantidade de combustível restante na bomba.
def bombaGasolina(self):
    self.volume_bomba = self.volume_bomba - self.quantidade_combustivel
    return self.volume_bomba

def bombaAlcool(self):
    self.volume_bomba = self.volume_bomba - self.quantidade_combustivel
    return self.volume_bomba

def bombaDisel(self):
    self.volume_bomba = self.volume_bomba - self.quantidade_combustivel
    return self.volume_bomba

def bombaGasNatural(self):
    self.volume_bomba = self.volume_bomba - self.quantidade_combustivel
    return self.volume_bomba
    
#envia a mensagem de entrada:    
def mensagem_entrada():
    print(f'Olá, essa é uma calculadora para combustivéis: ')
    print(f'  -> Para o cálculo utilizando quantidade de combustível. Digite >> c <<  ')
    print(f'  -> Para o cálculo utilizando o valor a ser pago. Digite >> vp << ')
    print(f'  -> Para o cálculo da quantidade de litro de combustível, digite >> lc << ')

#envia a mensagem pra escolha do combustivel:    
def mensagem_combustivel():
    print(f'Qual combustível você quer abastecer? ')
    print(f'  -> Para abastecer com gasolina digite >> gaso << ')
    print(f'  -> Para abastecer com Alcool digite >> alco << ')
    print(f'  -> Para disel, digite >> disel << ')
    print(f'  -> Para gás natural, digite >> gasn << ')


#looping de entrada do programa; escolha de forma de abastecimento:
while True:
    mensagem_entrada()
    pergunta_inicial = str(input(f"  -> Ou digite >> esc << para sair: "))
    if pergunta_inicial.lower() == "c":
        print (f'Ok, vamos calcular valores/quantidades pela quantidade de combustível.')
        # looping de escolha de tipos de combustíveis:
        while True:
            mensagem_combustivel()     
            pergunta_combustivel = str (input(f'  -> Ou escreva >> esc << pra sair '))
            if pergunta_combustivel.lower() == "gaso":
                #método que precifica o valor da gasolina:
                valor_gasolina = BombaCombustivel() 
                valor = 5.899
                valor_gasolina.alterarValor(float(valor))
                #método que define quantidade de combustível a ser colocado:
                valor_gasolina.quantidade_combustivel = float(input(f'Qual a quantidade de combustível a ser colocado?  '))
                # cálculo para obtenção de valor de pagamento 
                valor_gasolina.abastecerPorLitro()
                print(f'O valor a ser pago para adquirir {valor_gasolina.quantidade_combustivel} litros de gasolina é {valor_gasolina.valor_pago} reais')
                exit()

            elif pergunta_combustivel.lower() == 'alco':
                valor_alcool = BombaCombustivel() 
                valor = 3.899
                valor_alcool.alterarValor(float(valor))               
                valor_alcool.quantidade_combustivel = float(input(f'Qual a quantidade de combustível a ser colocado?  '))                
                valor_alcool.abastecerPorLitro()            
                print(f'O valor a ser pago para adquirir {valor_alcool.quantidade_combustivel} litros de gasolina é {valor_alcool.valor_pago} reais')
                exit()

            elif pergunta_combustivel.lower() == 'disl':                
                valor_disel = BombaCombustivel() 
                valor = 4.899
                valor_disel.alterarValor(float(valor))               
                valor_disel.quantidade_combustivel = float(input(f'Qual a quantidade de combustível a ser colocado?  '))                
                valor_disel.abastecerPorLitro()            
                print(f'O valor a ser pago para adquirir {valor_disel.quantidade_combustivel} litros de gasolina é {valor_disel.valor_pago} reais')
                exit()

            elif pergunta_combustivel.lower() == 'gasn':                
                valor_gasnatural = BombaCombustivel() 
                valor = 5.899
                valor_gasnatural.alterarValor(float(valor))                
                valor_gasnatural.quantidade_combustivel = float(input(f'Qual a quantidade de combustível a ser colocado?  '))                
                valor_gasnatural.abastecerPorLitro()            
                print(f'O valor a ser pago para adquirir {valor_gasnatural.quantidade_combustivel} litros de gasolina é {valor_gasnatural.valor_pago} reais')
                exit()

            elif pergunta_combustivel.lower() == "esc":
                print (f'Ok, tchau!')
                exit()

            print(f'Você digitou a opção errada. Digite a opção correta!')           
    
    elif pergunta_inicial.lower() == 'vp':
        print (f'Ok, vamos calcular valores/quantidades pelo valor a ser pago.')
        mensagem_combustivel()
        pergunta_combustivel = str (input(f'  -> Ou escreva >> esc << pra sair '))



    elif pergunta_inicial.lower() == 'lc':
        print (f'Ok, vamos calcular valores/quantidades pelo litro de combustível.')
    
    elif pergunta_inicial.lower() == "esc":
        print (f'Ok, tchau!')
        exit()
    
    print (f'Você digitou uma opção errada, digite a opção correta.')

 
                   
