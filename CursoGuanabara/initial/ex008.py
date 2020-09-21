medida = float(input('Digite uma medida em metros: '))
km = medida / (10 ** 3)
hm = medida / (10 ** 2)
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000
print(f'A medida em km é {km} | \t em hm é {hm} | \t em dam é {dam} | \t em metros é {medida} | \t em dm é {dm} | \t em cm é {cm} | \t em mm é {mm}')