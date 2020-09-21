def notas(*num, sit=False):
    """Receberá uma quantidade de notas de uma turma, retornando de volta a média das notas,
    o total de notas, a maior e a menor nota e, caso selecionado sit=True, a situação da turma em geral."""
    listaNum = []
    for numb in num:
        listaNum.append(numb)
    #Daqui pra cima é desnecessário porque o *num se comporta como uma tupla e pode ser manipulada com max(num)
    total = len(listaNum)
    totalSoma = sum(listaNum)
    dicionotas = {'total:' : total,
    'maior' : max(listaNum),
    'menor' : min(listaNum),
    'média' : totalSoma/total
    }
    if sit == True:
        if dicionotas['média'] >= 7:
            dicionotas['situação:'] = 'Boa'
        else:
            dicionotas['situação:'] = 'Ruim'
    return print(dicionotas)

notas(2, 7, 4, 6, 3.5, 2, sit=True)