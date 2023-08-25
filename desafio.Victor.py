"""""
Programa que calcule o salário de 3 funcionários:
    desenvolvedores (DEV):
        recebem +10% se ganharem mais de 3000 e +20% se ganharem menos de 3000
    DBA'S
    TESTER
        recebem +15% se ganharem mais de 3000 e +20% se ganharem menos de 3000. 
"""

def mensagem_entrada():
    print(f'Olá usuário,para calcular seu salário, escolha primeiro o seu cargo: ')
    print(f'desenvolvedor (D), DBAs (B) e para Tester (T).')
    
def cal_mais_dez():
    aux3 = aux2 * 0.1
    return aux3 + aux2

def cal_mais_quinze():
    aux3 = aux2 * 0.2
    return aux3 + aux2

def cal_mais_vinte():
    aux3 = aux2 * 0.2
    return aux3 + aux2

while True:
    mensagem_entrada()
    aux1 = str(input(f'Ou digite >> esc << para sair  ')) 
    if aux1.lower() == "D":
        aux2 = float(input(f'Agora digite quanto você ganha de salário'))
        if aux2 >= 3000:
            cal_mais_dez()
            print(f'O valor que você irá ganhar é {cal_mais_dez()}')
            exit()
        else:
            cal_mais_vinte()
            print(f'O valor que você irá ganhar é {cal_mais_vinte()}')  
            exit()       
    elif aux1.lower() == "B" or "T" :
        aux2 = float(print(f'Agora digite quanto você ganha de salário'))
        if aux2 >= 3000:
            cal_mais_quinze()
            print(f'O valor que você irá ganhar é {cal_mais_quinze()}')
            exit()
        else: 
            cal_mais_vinte()
            print(f'O valor que você irá ganhar é {cal_mais_vinte()}')  
            exit() 
    elif aux1.lower() == "esc":
        print(f'Ok, tchau!')
        exit()
    else:
        print(f'Você digitou uma opção errada. Larga de ser burro e faz sá porra direito!')

     
