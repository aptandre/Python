nota = float(input('Digite a nota do aluno: '))
nota2 = float(input('Digite a segunda nota do aluno: '))
media = (nota + nota2) / 2
if nota >= 9 and media <= 10:
    print(f'As notas foram {nota} e {nota2}, a média foi {media:.1f} \nStatus: Aprovado \nConceito A')
if nota >= 7.5 and media < 9:
    print(f'As notas foram {nota} e {nota2}, a média foi {media:.1f} \nStatus: Aprovado \nConceito B')
if nota >= 6 and media < 7.5:
    print(f'As notas foram {nota} e {nota2}, a média foi {media:.1f} \nStatus: Aprovado \nConceito C')
if nota >= 4.5 and media < 6:
    print(f'As notas foram {nota} e {nota2}, a média foi {media:.1f} \nStatus: Reprovado \nConceito D')
if nota >= 0 and media < 4:
    print(f'As notas foram {nota} e {nota2}, a média foi {media:.1f} \nStatus: Reprovado \nConceito E')