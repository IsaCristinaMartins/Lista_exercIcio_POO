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
    def __init__ (self, tipo_combustivel=str, valorLitro=float, quantidade_combustivel=int, valor_pago=float, volume_bomba=float):
        self.tipo_combustivel = tipo_combustivel
        self.valorLitro = valorLitro
        self.quantidade_combustivel = quantidade_combustivel 
        self.valor_pago = valor_pago
        self.volume_bomba = volume_bomba
        
    
# método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
    def abastecerPorValor(self):
        self.quantidade_combustivel = self.valor_pago / self.valorLitro
        return self.quantidade_combustivel
    
# método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
    def abastecerPorLitro(self, valorLitro=float, quantidade_combustivel=int):
        self.valor_pago = (self.valorLitro) * (self.quantidade_combustivel)
        return float(self.valor_pago)

# altera o valor do litro do combustível.
    def alterarValor(self, novoValorLitro=float): 
        self.valorLitro = novoValorLitro
        return self.valorLitro

# altera o tipo do combustível.
    def alterarCombustivel(self, outroCombustivel):
        self.tipo_combustivel = outroCombustivel
        return self.tipo_combustivel

# altera a quantidade de combustível restante na bomba.
    def alterarQuantidadeCombustivel(self):
        self.volume_bomba = self.volume_bomba - self.quantidade_combustivel
        return self.volume_bomba
    
#envia a mensagem de entrada:    
    def mensagem_entrada(self):
        print(f'Olá, essa é uma calculadora para combustivéis: ')
        print(f'  -> Para o cálculo utilizando quantidade de combustível. Digite >> c <<  ')
        print(f'  -> Para o cálculo utilizando o valor a ser pago. Digite >> vp << ')
        print(f'  -> Para o cálculo da quantidade de litro de combustível, digite >> lc << ')

#envia a mensagem pra escolha do combustivel:    
    def mensagem_combustivel(self):
        print(f'Qual combustível você quer abastecer? ')
        print(f'  -> Para abastecer com gasolina digite >> gaso << ')
        print(f'  -> Para abastecer com Alcool digite >> alco << ')
        print(f'  -> Para disel, digite >> disel << ')
        print(f'  -> Para gás natural, digite >> gasn << ')


#looping de entrada do programa; escolha de forma de abastecimento:
while True:
    mensagem1 = BombaCombustivel(None, None, None, None, None)
    mensagem1.mensagem_entrada()
    pergunta_inicial = str(input(f"  -> Ou digite >> esc << para sair: "))
    if pergunta_inicial.lower() == "c":
        print (f'Ok, vamos calcular valores/quantidades pela quantidade de combustível.')
        # looping de escolha de tipos de combustíveis:
        while True:
            mensagem2 = BombaCombustivel(None, None, None, None, None)
            mensagem2.mensagem_combustivel()     
            pergunta_combustivel = str (input(f'  -> Ou escreva >> esc << pra sair '))
            if pergunta_combustivel.lower() == "gaso":
                #método que precifica o valor da gasolina:
                valor_gasolina = BombaCombustivel(str, float, int, float, float ) 
                valor = 5.899
                valor_gasolina.alterarValor(float(valor))
                #método que define quantidade de combustível a ser colocado:
                pergunta_usuario = BombaCombustivel(str, float, int, float, float )
                pergunta_usuario.quantidade_combustivel(float(input(f'Qual a quantidade de combustível a ser colocado?  ')) )
                # cálculo para obtenção de valor de pagamento 
                resposta = BombaCombustivel(str, float, int, float, float )
                resposta.abastecerPorLitro()            
                print(f'O valor a ser pago para adquirir {pergunta_usuario} litros de gasolina é {resposta}')


           # elif pergunta_combustivel.lower() == 'alco':


            #elif pergunta_combustivel.lower() == 'disl':


#            elif pergunta_combustivel.lower() == 'gasn':


            elif pergunta_combustivel.lower() == "esc":
                print (f'Ok, tchau!')
                exit()
            
            print(f'Você digitou a opção errada. Digite a opção correta!')



           
    
   # elif pergunta_inicial.lower() == 'vp':
    #    print (f'Ok, vamos calcular valores/quantidades pelo valor a ser pago.')


    #elif pergunta_inicial.lower() == 'lc':
     #   print (f'Ok, vamos calcular valores/quantidades pelo litro de combustível.')
    
    elif pergunta_inicial.lower() == "esc":
        print (f'Ok, tchau!')
        exit()
    
    print (f'Você digitou uma opção errada, digite a opção correta.')

 
                   
