class Calculadoras:
    def PA(self, a1, r, n):
        self.a1 = a1
        self.r = r
        self.n = n
        an = a1 + ((n-1)*r)
        return an
            
    def Juros_C(self, C, i, n):
        M = C * ((1 + i)**n)
        return M

    def Velocidade_media(self, d, t):
        """D em metros e T em segundos!"""
        Vm = d / t
        return float(Vm)

    def Bhaskara(self, a, b, c):

        mdelta = (b ** 2) - (4 * a * c) 
        rDelta = mdelta ** (1/2)
        if rDelta < 0:
            print('Não há raízes reais para esta equação')
        if rDelta == 0:
            x0 = -b / (2*a)
            return x0
        if rDelta > 0:
            x1 = (-b + rDelta) // (2*a)    
            x2 = (-b - rDelta) // (2*a)
            return x1, x2

Calculadoras.Bhaskara(0, 1, -5, 6)
