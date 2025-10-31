import unittest


# Реалізувати клас для роботи з дробами
# чисельник - ціле число знаменник - ціле число,
# не ноль Створити - конструктор, який контролює
# валідність даних - рядкове представлення дробу
# - метод скорочення (4/6 -> 2/3) - математичні
# операції також з контролем як типів, так і
# даних після операцій здійснювати скорочення
# результату - методи числового представлення
# (як float) * метод створення з float представлення


class Fraction:
    def __init__(self, numerator: int, denominator: int):
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError("Numerator and Denominator should be numbers")
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")

        self.numerator = numerator
        self.denominator = denominator
        self.reduce()

    def reduce(self):
        gcf = self.greatest_common_factor(self.numerator, self.denominator)
        self.numerator //= gcf
        self.denominator //= gcf

        if self.denominator < 0:
            self.numerator *= -1
            self.denominator *= -1

    def greatest_common_factor(self, a, b):
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def __add__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("__add__ operation only works with numbers")

        return Fraction(self.numerator * other.denominator + other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("__sub__ operation only works with numbers")

        return Fraction(self.numerator * other.denominator - other.numerator * self.denominator,
                        self.denominator * other.denominator)

    def __mul__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("__mul__ operation only works with numbers")

        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            raise TypeError("__truediv__ operation only works with numbers")

        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return False

        return self.numerator == other.numerator and self.denominator == other.denominator

    def to_float(self):
        return self.numerator / self.denominator

    @classmethod
    def from_float(cls, value: float, precision: int = 1000000):
        if not isinstance(value, (float, int)):
            raise TypeError("Value should be a number")

        return Fraction(int(round(value * precision)), precision)


if __name__ == "__main__":
    # unittest.main()
    print("----------------------------------------")
    print(Fraction(10, 100))
    a1 = Fraction(10, 20)
    b1 = Fraction(2, 3)
    print(f"{a1} + {b1} = {a1 + b1}")
    print(f"{a1} - {b1} = {a1 - b1}")
    print(f"{a1} * {b1} = {a1 * b1}")
    print(f"{a1} / {b1} = {a1 / b1}")
    a2 = Fraction(123, 321)
    b2 = Fraction(123, 321)
    print(f"{a1} == {b1} = {a1 == b1}")
    print(f"{a2} == {b2} = {a2 == b2}")
    a025 = Fraction.from_float(0.25)
    a050 = Fraction.from_float(0.50)
    a075 = Fraction.from_float(0.75)
    a100 = Fraction.from_float(1.0)
    print("---- ---- ----")
    print(f"{0.25} = {a025}")
    print(f"{0.50} = {a050}")
    print(f"{0.75} = {a075}")
    print(f"{1.0} = {a100}")
    print("---- ---- ----")
    print(f"{a025} = {a025.to_float()}")
    print(f"{a050} = {a050.to_float()}")
    print(f"{a075} = {a075.to_float()}")
    print(f"{a100} = {a100.to_float()}")
    print("----------------------------------------")
