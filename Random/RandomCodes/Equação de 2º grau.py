def delta (a, b, c):
    return delta =  (b**2) - (4*a*c)
rDelta = delta **(1/2)
r1 = (-b + rDelta) / (2 * a)
r2 = (-b - rDelta) / (2 * a)
r0 = -b / (2 * a)

if delta > 0:
    print("O valor dessa miséria é: ", r1)
    print("O valor dessa carai é: ", r2)

elif delta == 0:
    print("O valor desse cu é: ", r0)
	
else:
    print("essa porra existe no conjunto dos reais.")
  
	
