from abc import ABC, abstractmethod
import random
import math


# Abstract class \ Interface

class Shape(ABC):
    
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    @abstractmethod
    def __str__(self):
        pass



# Implementations

class Square(Shape):

    def __init__(self, side_length: float):

        if side_length <= 0:
            raise ValueError("Side length must be positive.")
    
        self.side_length = side_length

    def area(self):
        return self.side_length ** 2
    
    def perimeter(self):
        return self.side_length * 4
    
    def __str__(self):
        return (f"Square(side_length={self.side_length}, "
                f"area={self.area():.2f}, perimeter={self.perimeter():.2f})")


class Circle(Shape):

    def __init__(self, radius: float):
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2
    
    def perimeter(self):
        return 2 * math.pi * self.radius
    
    def __str__(self):
        return (f"Circle(radius={self.radius}, "
                f"area={self.area():.2f}, perimeter={self.perimeter():.2f})")

    


class Triangle(Shape):
    
    def __init__(self, side_a : float, side_b: float, side_c: float):
        if side_a <=0 or side_b <=0:
            raise ValueError("Sides must be positive.")
        if side_c <= abs(side_a - side_b) or side_c >= (side_a + side_b):
            raise ValueError("Side c must be between |a-b| and a+b to form a valid triangle.")
        
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c 

    def area(self):
        s = (self.side_a + self.side_b + self.side_c) / 2
        return math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c))
    
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

    def __str__(self):
        return (f"Triangle(side_a={self.side_a}, side_b={self.side_b}, side_c={self.side_c}, "
                f"area={self.area():.2f}, perimeter={self.perimeter():.2f})")
    


class Trapezoid(Shape):

    def __init__(self, base_bottom: float, base_top: float, side_length: float):
        if base_bottom <= 0 or base_top <= 0:
            raise ValueError("Base lengths must be positive.")
        

        lower = (base_bottom - base_top) / 2
        upper = (base_bottom + base_top) / 2

        if not (lower <= side_length <= upper):
            raise ValueError(
                "Side length must be between (a−b)/2 and (a+b)/2 for a valid isosceles trapezoid."
            )
        
        self.base_bottom = base_bottom
        self.base_top = base_top
        self.side_length = side_length

    def area(self):
        return (self.base_bottom + self.base_top) * self.side_length / 2  # Deliberate mistake: Using side instead of height

    def perimeter(self):
        return self.base_bottom + self.base_top + 2 * self.side_length
    
    def __str__(self):
        return (f"Trapezoid(bottom={self.base_bottom}, top={self.base_top}, side={self.side_length}, "
                f"area={self.area():.2f}, perimeter={self.perimeter():.2f})")
    
     
def random_shape():

    choice = random.choice(["square", "circle", "triangle", "trapezoid"])

    if choice == "square":
        return Square(random.randint(1, 10))

    elif choice == "circle":
        return Circle(random.randint(1, 10))

    elif choice == "triangle":
        side_a = random.randint(1, 10)
        side_b = random.randint(1, 10)
        side_c = random.randint(abs(side_a - side_b) + 1, side_a + side_b - 1)  # Ensuring side_c is valid
        return Triangle(side_a, side_b, side_c)
    
    else:  # trapezoid

        # Bottom base chosen larger to ensure a valid trapezoid
        base_bottom = random.randint(6, 15)
        base_top = random.randint(1, base_bottom - 1)

        # Side length must be between the bounds (a−b)/2 to (a+b)/2 , converted to valid integer limits
        lower = math.ceil((base_bottom - base_top) / 2)          
        upper = math.floor((base_bottom + base_top) / 2)      

        side_length = random.randint(lower, upper)

        return Trapezoid(base_bottom, base_top, side_length)

def main():
    
    shape = random_shape()
    print(shape)


if __name__ == "__main__":

    main()
