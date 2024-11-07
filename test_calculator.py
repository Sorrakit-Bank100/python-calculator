import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-3,-2),-5)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(10,5),5)
    
    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(-5,-10),5)
    
    def test_multiply(self):
        self.assertEqual(self.calc.multiply(10,2),20)

    def test_multiply_zero(self):
        self.assertEqual(self.calc.multiply(2,0),0)

    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(-3,-2),6)
    
    def test_division(self):
        self.assertEqual(self.calc.divide(10,2),5)

    def test_division_zero(self):
        self.assertEqual(self.calc.divide(0,2),0)
    
    def test_modulo(self):
        self.assertEqual(self.calc.modulo(10,2),0)

    def test_modulo_zero(self):
        self.assertEqual(self.calc.modulo(0,10),0)

if __name__ == '__main__':
    unittest.main()