class MainChampion:
    def __init__(self, nome, rota, classe):
        self.nome = nome
        self.rota = rota
        self.classe = classe

lista_de_mains = [ MainChampion('Ahri', 'Meio', 'Assassin'),
                  MainChampion('Miss Fortune', 'Bot', 'Adcaster'),
                  MainChampion('Lux', 'Meio', 'Mage')]

class Buscador:
    def buscamain(self, lista, nome):
        str(nome)
        for i in range(len(lista)):
            if lista[i].nome == nome:
                return i
            return -1

    def vamos_buscar(self):
        lista = [ MainChampion('Ahri', 'Meio', 'Assassin'),
                  MainChampion('Miss Fortune', 'Bot', 'Adcaster'),
                  MainChampion('Lux', 'Meio', 'Mage')]
        
        onde_achou = self.buscamain(lista, 'Ahri')

        if onde_achou == -1:
            print("O main não está na playlist")
        else:
            mainchamp = lista_de_mains[onde_achou]
            print(mainchamp.nome, mainchamp.rota, mainchamp.classe, sep = ',')

#A maioria é mérito do Fabioh but there's still some work of mine in here too, because the code itself wasn't working
#Ahri = MainChampion('Ahri', 'Mid', 'Assassin')
#Lux = MainChampion('Lux', 'Mid', 'Mage')
#Miss_Fortune = MainChampion('Miss Fortune', 'Bot', 'ADC')
#lista = [Ahri, Lux, Miss_Fortune]
