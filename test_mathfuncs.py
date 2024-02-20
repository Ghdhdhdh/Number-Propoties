import unittest
import mathfuncs as mf

class TestMathFunctionMethods(unittest.TestCase):
    def test_abs(self):
        self.assertEqual(mf.absolute(-666), 666)
        self.assertEqual(mf.absolute(-6946), 6946)
        self.assertEqual(mf.absolute(666), 666)

    def test_negitive(self):
        self.assertEqual(mf.negitive(-677), True)
        self.assertEqual(mf.negitive(-8777), True)
        self.assertEqual(mf.negitive(-67), True)
        self.assertEqual(mf.negitive(677), False)
        self.assertEqual(mf.negitive(67), False)
        self.assertEqual(mf.negitive(677345), False)

    def test_power_of_2(self):
        self.assertEqual(mf.power_of_2(1), 0.0)
        self.assertEqual(mf.power_of_2(2), 1.0)
        self.assertEqual(mf.power_of_2(4), 2.0)
        self.assertEqual(mf.power_of_2(8), 3.0)
        self.assertEqual(mf.power_of_2(16), 4.0)
        self.assertEqual(mf.power_of_2(7), False)
        self.assertEqual(mf.power_of_2(3423), False)
        self.assertEqual(mf.power_of_2(10), False)

    def test_factors(self):
        self.assertEqual(mf.factors(5), [1,5])
        self.assertEqual(mf.factors(9), [1,3,9])
        self.assertEqual(mf.factors(5), [1,5])
        self.assertEqual(mf.factors(34), [1,2,17,34])


    def test_power_of_3(self):
        self.assertEqual(mf.power_of_3(3), 1.0)
        self.assertEqual(mf.power_of_3(9), 2.0)
        self.assertEqual(mf.power_of_3(27), 3.0)
        self.assertEqual(mf.power_of_3(81), 4.0)
        self.assertEqual(mf.power_of_3(243), 5.0)
        self.assertEqual(mf.power_of_3(44234), False)
        self.assertEqual(mf.power_of_3(44423434), False)
if __name__ == '__main__':
    unittest.main()