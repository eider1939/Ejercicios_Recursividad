import unittest
from Ejercicio1 import factorial
from Ejercicio2 import fibonacci
from Ejercicio3 import suma_digitos

class TestRecursividad(unittest.TestCase):

    def test_factorial(self):
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(0), 1)
        self.assertEqual(factorial(1), 1)

    def test_fibonacci(self):
        self.assertEqual(fibonacci(6), 8)
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_suma_digitos(self):
        self.assertEqual(suma_digitos(1234), 10)
        self.assertEqual(suma_digitos(0), 0)
        self.assertEqual(suma_digitos(9), 9)

if __name__ == '__main__':
    unittest.main()
