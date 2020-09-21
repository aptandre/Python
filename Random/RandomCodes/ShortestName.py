class Nome:
    lista = ['Ahri', 'Lux', 'Yasuo']
    lists = []
    def menor_nome(lista):
        fim = len(lista)
        for x in range(fim):
            petra = len(lista[x])
            if petra > len(lista[x + 1]):
                petra = lista[x + 1]
                x = x + 1
            return petra
            #else:
                #print("Deu erro hein mlk")
        #work on this later


def ShortestName (nomes):
    x = 1
    y = 1
    listinha = []
    while x <= len(nomes):
        ray = len(nomes[-1 + y])
        listinha.append(ray)
        y = y + 1
        x = x + 1
        dex = min(listinha)
    z = 1
    if dex != ray: #len(nomes[-1 + z])
        Deus = 182378732738
        while dex != Deus:
            Deus = len(nomes[-1 + z])
            z = z + 1

    return nomes[-2 + z]


#class Nome:
    #lists = []
    #fim = len(lista)
    #def menor_nome(self, lista):
        #fim = len(lista)
        #for x in range(fim):
           # petra = len(x)
            #if petra < len(x + 1):
                #petra = lista[x + 1]
                #return petra
            #else:
                #print("Deu erro hein mlk")
                
            
                
