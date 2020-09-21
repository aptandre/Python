'''Algumas anotações sobre strings!
-Para contá-los, considere-os como listas = BARRY = B0 A1 R2 R3 Y4 Isso também se aplica aos cortes Barry[1:3] 2 caracteres, começa no 1 e termina no 2 (3-1)
-Espaços também são contados em comandos como len() e count()
-Há diferenciação de maiúsculos para minúsculos!
-Lembre-se dos padrões [x:y:z] x = começo, y = fim - 1, z = restrição if z = 2: pula de 2 em 2. Ex: Barry[0:5:2] printa = Bry
-Também se aplica às estruturas de :5 (início ao 5) e 5: (5 ao fim) e também os [9::3] (começa no 9, vai até o final blank e pula 3 em 3)
-frase.count() contará quantas vezes determinado caractere ou palavra aparece.
-frase.find() dará a posição do string em que começa determinado parâmetro (se voltar -1, a string não existe na variável frase)
- 'HEY LOCA!' frase.replace('LOCA!', 'LOLA!')
-frase.strip() remove os espaços (exceto os entre letras) frase.rstrip() RIGHT e frase.lstrip()
-frase.split() divide a frase em n blocos em uma lista
-' '.join(frase) Esse comando une os elementos de uma lista com um espaço, que pode ser um hífen, com números, conectivos etc.'''
#test.swapcase() faz com que o que é maiúsculo vire minúsculo e vice-versa.

nome = input('Digite o nome: ').strip()
print(f'O seu nome capitalizado é {nome.upper()}')
print(f'O seu nome em letras minúsculas é {nome.lower()}')
x = nome.split()
print(f'O seu primeiro nome é {x[0]} e ele tem o tamanho de {len(x[0])} caracteres')
lay = i = 0
aye = len(x)
for y in range(aye):
    lay = lay + len(x[i])
print(f'O seu nome tem, ao todo, {lay} letras')
#Anotações do curso, para contar o nome sem os espaços entre eles tipo AJ Pieterce é só colocar len(nome) - nome.count(' ')
#Na variável do tanto de letras do primeiro nome dá pra colocar para encontrar o primeiro espaço nome.find(" ") que achará igualmente

