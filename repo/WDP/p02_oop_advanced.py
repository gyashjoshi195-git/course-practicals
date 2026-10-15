"""Practical 2: Inheritance, Polymorphism and Abstract Classes."""
from abc import ABC, abstractmethod
import math


# ---- Abstract class ----
class Shape(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    def describe(self):
        print(f"{self.name}: area={self.area():.2f}, perimeter={self.perimeter():.2f}")


# ---- Inheritance (single) ----
class Circle(Shape):
    def __init__(self, r):
        super().__init__("Circle")
        self.r = r

    def area(self):
        return math.pi * self.r ** 2

    def perimeter(self):
        return 2 * math.pi * self.r


class Rectangle(Shape):
    def __init__(self, l, b):
        super().__init__("Rectangle")
        self.l, self.b = l, b

    def area(self):
        return self.l * self.b

    def perimeter(self):
        return 2 * (self.l + self.b)


class Square(Rectangle):                 # multilevel inheritance
    def __init__(self, side):
        super().__init__(side, side)
        self.name = "Square"


# ---- Polymorphism via method overriding ----
class Employee:
    def __init__(self, name, salary):
        self.name, self.salary = name, salary

    def role(self):
        return "Employee"

    def bonus(self):
        return self.salary * 0.05


class Manager(Employee):
    def role(self):
        return "Manager"

    def bonus(self):
        return self.salary * 0.20


class Developer(Employee):
    def role(self):
        return "Developer"

    def bonus(self):
        return self.salary * 0.10


if __name__ == "__main__":
    # shape = Shape("x")   # TypeError: cannot instantiate abstract class
    for shape in [Circle(5), Rectangle(4, 6), Square(3)]:
        shape.describe()                 # same call, different behaviour

    print()
    for emp in [Employee("A", 30000), Manager("B", 80000), Developer("C", 60000)]:
        print(f"{emp.name:<3} {emp.role():<10} bonus = {emp.bonus():.0f}")
