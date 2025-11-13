

import math


# Base Class: Shape 

class Shape:
    """Abstract base class for all shapes."""

    def csa(self):
        """Method to calculate Curved Surface Area."""
        raise NotImplementedError("CSA method not implemented")

    def tsa(self):
        """Method to calculate Total Surface Area."""
        raise NotImplementedError("TSA method not implemented")

    def volume(self):
        """Method to calculate Volume."""
        raise NotImplementedError("Volume method not implemented")


# ==================================
# Class: Cylinder (Inherits Shape)
# ==================================
class Cylinder(Shape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def csa(self):
        # CSA = 2πrh
        return 2 * math.pi * self.radius * self.height

    def tsa(self):
        # TSA = 2πr(h + r)
        return 2 * math.pi * self.radius * (self.height + self.radius)

    def volume(self):
        # Volume = πr²h
        return math.pi * self.radius ** 2 * self.height


# ===============================
# Class: Cone (Inherits Shape)
# ===============================
class Cone(Shape):
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def csa(self):
        # CSA = πrl , where l = √(r² + h²)
        l = math.sqrt(self.radius ** 2 + self.height ** 2)
        return math.pi * self.radius * l

    def tsa(self):
        # TSA = πr(r + l)
        l = math.sqrt(self.radius ** 2 + self.height ** 2)
        return math.pi * self.radius * (self.radius + l)

    def volume(self):
        # Volume = (1/3)πr²h
        return (1 / 3) * math.pi * self.radius ** 2 * self.height


# ===============================
# Class: Cube (Inherits Shape)
# ===============================
class Cube(Shape):
    def __init__(self, side):
        self.side = side

    def csa(self):
        # CSA = 4a²
        return 4 * self.side ** 2

    def tsa(self):
        # TSA = 6a²
        return 6 * self.side ** 2

    def volume(self):
        # Volume = a³
        return self.side ** 3


# ===============================
# Class: Cuboid (Inherits Shape)
# ===============================
class Cuboid(Shape):
    def __init__(self, length, breadth, height):
        self.length = length
        self.breadth = breadth
        self.height = height

    def csa(self):
        # CSA = 2h(l + b)
        return 2 * self.height * (self.length + self.breadth)

    def tsa(self):
        # TSA = 2(lb + bh + lh)
        return 2 * (self.length * self.breadth +
                    self.breadth * self.height +
                    self.length * self.height)

    def volume(self):
        # Volume = l × b × h
        return self.length * self.breadth * self.height


# ===============================
# Class: Sphere (Inherits Shape)
# ===============================
class Sphere(Shape):
    def __init__(self, radius):
        self.radius = radius

    def csa(self):
        # CSA = TSA = 4πr²
        return 4 * math.pi * self.radius ** 2

    def tsa(self):
        # TSA = 4πr²
        return 4 * math.pi * self.radius ** 2

    def volume(self):
        # Volume = (4/3)πr³
        return (4 / 3) * math.pi * self.radius ** 3
