# Classe TV: Faça um programa que simule um televisor criando-o 
# como um objeto. O usuário deve ser capaz de informar o número do 
# canal e aumentar ou diminuir o volume. Certifique-se de que o número
# do canal e o nível do volume permanecem dentro de faixas válidas.

class Tv:
    def __init__(self, numero_canal, volume):
      self.numero_canal = numero_canal
      self.volume = volume
    
    def mudar_canal_frente(self, numero_canal):
       self.numero_canal = numero_canal +1
       if self.numero_canal>=20:
          print(f'canal errado')
          self.numero_canal = 19
          
       print (f'O canal agora é o {self.numero_canal}')
       return self.canal
    
    def mudar_canal_tras(self, numero_canal):
       self.numero_canal = numero_canal -1
       if self.numero_canal<=2:
          print(f'canal errado')
          self.numero_canal = 5

       print (f'O canal agora é o {self.numero_canal}')
       return self.numero_canal
    
    def nivel_do_volume_maior(self, volume):
       self.volume = volume +1
       if self.volume>=60:
          print(f'Cuidado, volume muito elevado!')
          self.volume = 59
       
       print (f'O volume agora é {self.volume}')
       return self.volume

    def nivel_do_volume_menor(self, volume):
       self.volume = self.volume -1
       if self.volume==0:
          print(f'>>  MUDO!  <<')

       print (f'O volume agora é {self.volume}')
       return self.volume
    
    def mudanca_direta(self, numero_canal, numero):
       numero = int (input(f'Digite aqui o canal desejado'))
       if numero >= 20:
          print(f'Canal inexistente')
          self.numero_canal = 19
       elif numero <=2:
          print(f'Canal inexistente')
          self.numero_canal = 5
        
       self.numero_canal = numero
       print(f'Direcionando o canal para {self.numero_canal}')

teste = Tv(10,34)

print(teste.nivel_do_volume_menor(1))
          
teste.nivel_do_volume_menor(1)
teste.nivel_do_volume_menor(1)
teste.nivel_do_volume_menor(1)
teste.nivel_do_volume_menor(1)
teste.nivel_do_volume_menor(1)

print(teste.nivel_do_volume_menor(1))


       
      


    