from math import gcd


class Fraction:
    """A class representing fractions."""

    def __init__(self, numerator: int, denominator: int):
        if type(numerator) is not int:
            raise TypeError("Numerator must be an integer.")

        if type(denominator) is not int:
            raise TypeError("Denominator must be an integer.")

        if denominator <= 0:
            raise ValueError("Denominator must be positive.")

        divisor = gcd(numerator, denominator)

        self.numerator = numerator // divisor
        self.denominator = denominator // divisor

    def __eq__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        return (
            self.numerator * other.denominator
            == other.numerator * self.denominator
        )

    def __ne__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        return (
            self.numerator * other.denominator
            != other.numerator * self.denominator
        )
    def __lt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        return (
            self.numerator * other.denominator
            < other.numerator * self.denominator
        )

    def __le__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        return (
            self.numerator * other.denominator
            <= other.numerator * self.denominator
        )

    def __gt__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        return (
            self.numerator * other.denominator
            > other.numerator * self.denominator
        )

    def __ge__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        return (
            self.numerator * other.denominator
            >= other.numerator * self.denominator
        )

    def __add__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        numerator = (
            self.numerator * other.denominator
            + other.numerator * self.denominator
        )

        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    def __sub__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        numerator = (
            self.numerator * other.denominator
            - other.numerator * self.denominator
        )

        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)
    def __mul__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        numerator = self.numerator * other.numerator

        denominator = self.denominator * other.denominator

        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        if not isinstance(other, Fraction):
            return NotImplemented

        if other.numerator == 0:
            raise ZeroDivisionError("Cannot divide by zero.")

        numerator = self.numerator * other.denominator

        denominator = self.denominator * other.numerator

        if denominator < 0:
            numerator = -numerator
            denominator = -denominator

        return Fraction(numerator, denominator)