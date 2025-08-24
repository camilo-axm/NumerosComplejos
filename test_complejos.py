import unittest
import math
import complejos as cx

class TestComplejos(unittest.TestCase):

    def test_suma(self):
        self.assertEqual(cx.suma((1,2), (3,4)), (4,6))
        self.assertEqual(cx.suma((-1,-1), (1,1)), (0,0))

    def test_resta(self):
        self.assertEqual(cx.resta((5,3), (2,1)), (3,2))
        self.assertEqual(cx.resta((0,0), (1,1)), (-1,-1))

    def test_producto(self):
        self.assertEqual(cx.producto((1,2), (3,4)), (-5,10))
        self.assertEqual(cx.producto((0,1), (0,1)), (-1,0))

    def test_division(self):
        self.assertEqual(cx.division((1,1), (1,-1)), (0.0,1.0))
        self.assertAlmostEqual(cx.division((3,2), (4,-3))[0], 0.24, places=2)
        self.assertAlmostEqual(cx.division((3,2), (4,-3))[1], 0.68, places=2)

    def test_modulo(self):
        self.assertEqual(cx.modulo((3,4)), 5)
        self.assertEqual(cx.modulo((0,0)), 0)

    def test_conjugado(self):
        self.assertEqual(cx.conjugado((3,4)), (3,-4))
        self.assertEqual(cx.conjugado((1,-1)), (1,1))

    def test_fase(self):
        self.assertAlmostEqual(cx.fase((1,1)), math.pi/4, places=5)
        self.assertAlmostEqual(cx.fase((0,1)), math.pi/2, places=5)

    def test_cartesiano_a_polar(self):
        r, theta = cx.cartesiano_a_polar((1,1))
        self.assertAlmostEqual(r, math.sqrt(2), places=5)
        self.assertAlmostEqual(theta, math.pi/4, places=5)

    def test_polar_a_cartesiano(self):
        c = cx.polar_a_cartesiano((math.sqrt(2), math.pi/4))
        self.assertAlmostEqual(c[0], 1.0, places=5)
        self.assertAlmostEqual(c[1], 1.0, places=5)

if __name__ == "__main__":
    unittest.main()
