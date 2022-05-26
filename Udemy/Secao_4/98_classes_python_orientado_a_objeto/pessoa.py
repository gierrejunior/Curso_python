# class Pessoa: # Quando a função está dentro de uma classe, ela é o método dessa classe
#     def falar(self): # o self serve pra dizer que, quando eu coloca p1.falar()  é a mesma coisa de dizer p1.falar(p1), a instancia está chamando ela mesma
#         print('Pessoa está falando')
        
        
#!-------------------------------------------------------------------------------------------------------------------------------------------------------------
from datetime import datetime

class Pessoa:
    ano_atual = int(datetime.now().year)
    
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.nome = nome
        self.idade = idade
        self.comendo = comendo
        self.falando = falando
        
    def falar(self, assunto):
        if self.comendo:
            print(f'{self.nome} nao pode falar comendo')
            return
        
        if self.falando:
            print(f'{self.nome} ja está falando')
            return
        
        print(f'{self.nome} está falando sobre {assunto}')
        self.falando = True
        
    
    def parar_falar(self):
        if not self.falando:
            print(f'{self.nome} não está falando')
            return
        
        if self.comendo:
            print(f'{self.nome} não está falando, pois ele está comendo')
            return
        
        print(f'{self.nome} parou de falar')
        self.comendo = False 
                

    def comer(self, alimento):
        if self.comendo:
            print(f'{self.nome} já está comendo.')
            return
        
        if self.falando:
            print(f'{self.nome} não pode comer, pois ele está falando')
            return
        
        print(f'{self.nome} está comendo {alimento}.')
        self.comendo =True
        
    
    def parar_comer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo')
            return
        
        if self.falando:
            print(f'{self.nome} está falando, logo não está comendo')
                
        print(f'{self.nome} parou de comer')
        self.comendo = False

    def get_ano_nascimento(self):
        ano_nascimento = self.ano_atual - self.idade
        
        return ano_nascimento