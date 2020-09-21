import Calculator
'''Pay attention to the structures! É muito importante que haja "test_" nos métodos da classe de testes
e é fundamental, também, que o arquivo seja salvo como test_something.py
Para executar o código, é só ir no cmd >cd (caso esteja no diretório errado) e depois colocar py.test test.something.py'''
class TestCalculator:

    def test_Calculator(self):
        b = Calculator.Calculadoras()
        assert b.PA(1,5,5) == (21)

    def test_Calculator2(self):
        b = Calculator.Calculadoras()
        assert b.PA (0,0,0) == (0)

    def test_Calculator3(self):
        b = Calculator.Calculadoras()
        assert b.PA (10, -3, 7) == (-8)

    def test_Calculator4(self):
        b = Calculator.Calculadoras()
        assert b.Juros_C(10000, 0.5, 6) == (113906.25)

    def test_Calculator5(self):
        b = Calculator.Calculadoras()
        assert b.Juros_C (5000, 0.35, 10) == (100532.7793430904)

    def test_Calculator6(self):
        b = Calculator.Calculadoras()
        assert b.Velocidade_media(1235, 2) == (617.5)

    def test_Calculator7(self):
        b = Calculator.Calculadoras()
        assert b.Bhaskara(1, -5, 6) == (3, 2)
