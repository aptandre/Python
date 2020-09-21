class Calculadoras:

        def PA(a1, r, n):
            an = a1 + ((n-1)*r)
            return an
            
        def Juros_C(C, i, n):
            M = C * ((1 + i)**n)
            return M

        def Velocidade_media(d, t):
            """D em metros e T em segundos!"""
            Vm = d // t
            return Vm

        def Bhaskara(a, b, c):
            delta = b ** 2 - 4 * a * c 
            rDelta = delta ** (1/2)
            if delta < 0:
                print('Não há raízes reais para esta equação')
            if rDelta == 0:
                x0 = -b / (2*a)
                return x0
            if rDelta > 0:
                x1 = - b + rDelta // (2*a)    
                x2 = - b - rDelta // (2*a)
                return x1, x2    
