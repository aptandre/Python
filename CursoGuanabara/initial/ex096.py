largura = float(input("Digite a largura: "))
altura = float(input("Digite a altura: "))
def área (largura, altura):
    area = largura * altura
    return (area)
print(f'A área de um terreno {largura}m por {altura}m é {área(largura, altura)}m²')