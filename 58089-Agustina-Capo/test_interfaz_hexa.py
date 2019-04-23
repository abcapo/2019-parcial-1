import unittest
from  import 

class TestInterfazFactorial(unittest.TestCase):
    def test_interfaz_5(self):
        result = interfaz_hexa ('5')
        self.assertEqual(result, 5)
    def test_interfaz_hola(self):
        result = interfaz_hexa('hola')
        self.assertEqual(result, 'error')
if __name__ == '__main__':
    unittest.main()