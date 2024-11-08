from __future__ import annotations
from math import sqrt

class Vector:
    def __init__(self, x: float, y: float, z: float = 0):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"Vector({self.x}, {self.y}, {self.z})"

    def __bool__(self):
        return not (self.x == 0 and self.y == 0 and self.z == 0)

    def __len__(self):
        return 3 

    def __getitem__(self, index: int):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        else:
            raise IndexError("Index out of range")

    def __setitem__(self, index: int, value: float):
        if index == 0:
            self.x = value
        elif index == 1:
            self.y = value
        elif index == 2:
            self.z = value
        else:
            raise IndexError("Index out of range")

    def __add__(self, other: Vector) -> Vector:
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other: Vector) -> Vector:
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x * other.x, self.y * other.y, self.z * other.z)
        else:
            return Vector(self.x * other, self.y * other, self.z * other)

    def __truediv__(self, scalar: float) -> Vector:
        return Vector(self.x / scalar, self.y / scalar, self.z / scalar)

    def __eq__(self, other: Vector) -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __neg__(self) -> Vector:
        return Vector(-self.x, -self.y, -self.z)

    def __abs__(self) -> float:
        return sqrt(self.x**2 + self.y**2 + self.z**2)


# Instantiation
v1 = Vector(1, 4, 6)
print(v1)              # Expected Output: Vector(1, 4, 6)

# Boolean Evaluation
print(bool(v1))               # Expected Output: True
print(bool(Vector(0, 0, 0)))  # Expected Output: False

# Length
print(len(v1))                # Expected Output: 3

# Indexing and Slicing
print(v1[1])                  # Expected Output: 4
v1[1] = 10
print(v1)                     # Expected Output: Vector(1, 10, 6)

# Vector Arithmetic
v2 = Vector(3, 7, 2)
print(v1 + v2)                # Expected Output: Vector(4, 17, 8)
print(v1 - v2)                # Expected Output: Vector(-2, 3, 4)
print(v1 * v2)                # Expected Output: Vector(3, 70, 12)

# Scalar Multiplication and Division
print(v1 * 3)                 # Expected Output: Vector(3, 30, 18)
print(v1 / 2)                 # Expected Output: Vector(0.5, 5, 3)

# Absolute Value (Norm)
print(abs(v1))                # Expected Output: √(1^2 + 10^2 + 6^2) = 11.66...

# Equality Comparison
print(v1 == Vector(1, 10, 6)) # Expected Output: True

# Negation
print(-v1)                    # Expected Output: Vector(-1, -10, -6)