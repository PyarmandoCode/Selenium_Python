import unittest

class MiPrueba(unittest.TestCase):
    def test_suma(self):
        resultado=2+3
        #todo verificar los resultados del metodo suma
        self.assertEqual(resultado,5)#Comprueba si es resultado es optimo
    def test_resta(self):
        resultado =5-3
        self.assertEqual(resultado,2)
    def test_division(self):
        resultado=6/2
        self.assertEqual(resultado,3)

if __name__=="__main__":
    unittest.main()
