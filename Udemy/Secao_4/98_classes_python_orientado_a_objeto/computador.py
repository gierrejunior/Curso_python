class Computador:
    def __init__(self, marca = 'Asus', memoria_ram = '8gb', placa_de_video = 'Nvidia' ):
        self.marca = marca
        self.memoria_ram = memoria_ram
        self.placa_de_video =  placa_de_video    
    
    
    def Ligar(self):
        print('estou ligando')
        
    def Desligar(self):
        print('Estou desligando')
        
    def ExibirInformacoesDesteComputador(self):
        print(self.marca, self.memoria_ram, self.placa_de_video)