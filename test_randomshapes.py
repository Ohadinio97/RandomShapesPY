import unittest
from random_shapes import Circle, Trapezoid, Square, Triangle, random_shape
import math
import random




class TestShapes(unittest.TestCase):

    def test_square(self):
        side = 4
        square = Square(side)
        self.assertEqual(square.area(), side ** 2)
        self.assertEqual(square.perimeter(), 4 * side)
        self.assertEqual(square.side_length, side)

    def test_invalid_square(self):
        with self.assertRaises(ValueError):
            Square(0)
        with self.assertRaises(ValueError):
            Square(-5)


    
    def test_circle(self):
        radius = 3
        circle = Circle(radius)
        self.assertAlmostEqual(circle.area(), math.pi * radius ** 2)
        self.assertAlmostEqual(circle.perimeter(), 2 * math.pi * radius)
        self.assertEqual(circle.radius, radius)

    def test_invalid_circle(self):
        with self.assertRaises(ValueError):
            Circle(0)
        with self.assertRaises(ValueError):
            Circle(-7)


    
    def test_triangle(self):
        side_a = 3
        side_b = 4
        side_c = 5
        triangle = Triangle(side_a, side_b, side_c)
        self.assertEqual(triangle.side_a, side_a)
        self.assertEqual(triangle.side_b, side_b)
        self.assertEqual(triangle.side_c, side_c)
        self.assertEqual(triangle.perimeter(), side_a + side_b + side_c)

        s = (side_a + side_b + side_c) / 2
        correct_area = math.sqrt(s * (s - side_a) * (s - side_b) * (s - side_c))
        self.assertAlmostEqual(triangle.area(), correct_area)

    def test_invalid_triangle(self):
        with self.assertRaises(ValueError):
            Triangle(0, 4, 5)
        with self.assertRaises(ValueError):
            Triangle(3, -4, 5)
        with self.assertRaises(ValueError):
            Triangle(1, 2, 10)  


    
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

    def test_invalid_trapezoid(self):
        with self.assertRaises(ValueError):
            Trapezoid(0, 4, 5)
        with self.assertRaises(ValueError):
            Trapezoid(10, -4, 5)
        with self.assertRaises(ValueError):
            Trapezoid(10, 5, 2)  # Side length too short
        with self.assertRaises(ValueError):
            Trapezoid(10, 4, 20)  # Side length too long


    
    # Test for random shape generator
    def test_random_shape(self):

        random.seed(0)  # For consistency in tests

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

