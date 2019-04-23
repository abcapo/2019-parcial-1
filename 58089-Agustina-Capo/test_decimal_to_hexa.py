import unittest
from deci_to_hexa import decimal_to_hexa

class TestDeciToHexa(unittest.TestCase):
    def test_deci_to_hexa_5(self):
        hexa_number = decimal_to_hexa(5)
        self.assertEqual(hexa_number,'5')
    def test_deci_to_hexa_10(self):
        hexa_number = decimal_to_hexa(10)
        self.assertEqual(hexa_number,'A')
    def test_deci_to_hexa_17(self):
        hexa_number = decimal_to_hexa(17)
        self.assertEqual(hexa_number,'11')
    def test_deci_to_hexa_16(self):
        hexa_number = decimal_to_hexa(16)
        self.assertEqual(hexa_number,'10')
    def test_deci_to_hexa_4095(self):
        hexa_number = decimal_to_hexa(4095)
        self.assertEqual(hexa_number,'FFF')
    def test_deci_to_hexa_1234(self):
        hexa_number = decimal_to_hexa(1234)
        self.assertEqual(hexa_number,'4D2')
    def test_deci_to_hexa_234(self):
        hexa_number = decimal_to_hexa(234)
        self.assertEqual(hexa_number,'EA')

if __name__ == "__main__":
    unittest.main()