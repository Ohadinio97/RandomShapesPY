import unittest
from shapes import Circle, Trapezoid, Square, Triangle, random_shape
import math


class TestShapes(unittest.TestCase):


    def test_square(self):
        side = 4
        square = Square(side)
        self.assertEqual(square.area(), side ** 2)
        self.assertEqual(square.perimeter(), 4 * side)
        self.assertEqual(square.side_length, side)

    def test_circle(self):
        radius = 3
        circle = Circle(radius)
        self.assertAlmostEqual(circle.area(), math.pi * radius ** 2)
        self.assertAlmostEqual(circle.perimeter(), 2 * math.pi * radius)
        self.assertEqual(circle.radius, radius)



    def test_triangle(self):
        side = 5
        triangle = Triangle(side)
        self.assertAlmostEqual(triangle.area(), math.sqrt(3) * side**2 / 4)
        self.assertEqual(triangle.perimeter(), 3 * side)
        self.assertEqual(triangle.side_length, side)


    def test_trapezoid(self):
        base_bottom = 10
        base_top = 4
        side = 6
        trapezoid = Trapezoid(base_bottom, base_top, side)

        self.assertEqual(trapezoid.perimeter(), base_bottom + base_top + 2 * side)

        # Calculate the correct area
        height = math.sqrt(side**2 - ((base_bottom - base_top) / 2) ** 2)
        correct_area = (base_bottom + base_top) * height / 2
        self.assertNotAlmostEqual(trapezoid.area(), correct_area)

        # Check that the side length is valid for the given bases
        lower = (base_bottom - base_top) / 2
        upper = (base_bottom + base_top) / 2
        self.assertGreaterEqual(side, lower)
        self.assertLessEqual(side, upper)



    # Test for random shape generator
    def test_random_shape(self):
        for _ in range(100):
            shape = random_shape()
            self.assertIsInstance(shape, (Square, Circle, Triangle, Trapezoid))

            if isinstance(shape, Trapezoid):
                 lower = (shape.base_bottom - shape.base_top) / 2
                 upper = (shape.base_bottom + shape.base_top) / 2

                 self.assertGreaterEqual(shape.side_length, lower)
                 self.assertLessEqual(shape.side_length, upper)


        

if __name__ == "__main__":
    unittest.main()
