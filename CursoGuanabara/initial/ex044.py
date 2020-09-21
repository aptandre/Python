#Dei uma adaptada nesse exercício
print('=' * 25)
valor = float(input('Digite o valor do produto: '))
print('=' * 25)
print(f'Essas são as formas de pagamento disponíveis: \n1-À vista no dinheiro ou no cheque com 10% de desconto e o preço ficará por {valor - (valor*0.1)} \n2-À vista no cartão com 5% de desconto, ficará por {valor - (valor*0.05)}; \n3-Em 2x no cartão pelo preço normal, duas parcelas de {valor/2} \n4-A partir de 3x no cartão, serão cobrados 20% de juros até um máximo de 9 meses. ')
print('=' * 25)
options = int(input('E então, qual das opções será a escolhida? '))
while options < 0 or options > 4:
    options = int(input('Opção inválida, qual das opções será a escolhida? '))
if options == 1:
    print(f'CONFIRMADO! Você irá pagar o valor de {valor - (valor*0.1)}')
elif options == 2:
    print(f'CONFIRMADO! Você irá pagar o valor de {valor - (valor * 0.05)}')
elif options == 3:
    print(f'CONFIRMADO! Você irá pagar o valor de {valor / 2} por parcela.')
elif options == 4:
    parcelas = int(input("Digite o número de vezes que deseja parcelar: "))
    while parcelas > 9 or parcelas < 0:
        parcelas = int(input("Número inválido. Digite o número de vezes que deseja parcelar: "))
    print(f'Você irá pagar o valor de {((valor + (valor * 0.2)) /parcelas):.1f} por {parcelas} parcelas nesse produto.')