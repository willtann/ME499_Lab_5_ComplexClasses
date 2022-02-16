#! /Users/tannerwilliams/Desktop/ME499/ME499_Lab_5_ComplexClasses/complex.py


class Complex:
    """
    This is a class for manipulating and creating complex numbers.
    Inputs:
        - self.re = integer or float representing real number
        - self.im = integer or float representing imaginary number
    Outputs:
        - Complex form of the inputs
        - Operations on multiple inputs
    """

    def __init__(self, re=0.0, im=0.0):
        # If user inputted int, convert to float
        if not type(re) == float:
            self.re = float(re)
        else:
            self.re = re

        if not type(im) == float:
            self.im = float(im)
        else:
            self.im = im

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        if self.im < 0:
            return '(' + self.re.__str__() + " " + '-' + " " + abs(self.im).__str__() + 'i' ')'
        else:
            return '(' + self.re.__str__() + " " + '+' + " " + abs(self.im).__str__() + 'i' ')'

    def __add__(self, other):
        # Make complex number whether user inputted float or int
        if type(other) == int:
            other = Complex(other)
        if type(other) == float:
            other = Complex(other)
        else:
            other = other
        # Add and convert to final complex form
        return Complex(self.re + other.re, self.im + other.im)

    def __radd__(self, other):
        # Commutative
        return self.__add__(Complex(other))

    def __mul__(self, other):
        # Make complex number whether user inputted float or int
        if type(other) == int:
            other = Complex(other)
        if type(other) == float:
            other = Complex(other)
        # form (self.re * other.re) + (self.re * other.im) + (self.im * other.re) + (self.im * other.im)
        return Complex(((self.re * other.re) - (float(self.im) * float(other.im))),
                       (self.re * float(other.im)) + (float(self.im) * other.re))

    def __rmul__(self, other):
        # Commutative
        return self.__mul__(Complex(other, 0.0))

    def __truediv__(self, other):
        # Make complex number whether user inputted float or int
        if type(other) == int:
            other = Complex(other)
        if type(other) == float:
            other = Complex(other)
        # making things easier with representative variables in individual non-complex forms
        a = self.re
        b = float(self.im)
        c = other.re
        d = float(other.im)
        # Calculate and convert back to complex form
        return Complex((((a * c)+(b * d)) / ((c**2)+(d**2))), (((b * c)-(a * d)) / ((c**2)+(d**2))))

    def __rtruediv__(self, other):
        # Non-commutative
        return (Complex(other)).__truediv__(self)

    def __sub__(self, other):
        # Make complex number whether user inputted float or int
        if type(other) == int:
            other = Complex(other)
        if type(other) == float:
            other = Complex(other)
        # Subtracting and converting to final complex form
        return Complex(self.re - other.re, self.im - other.im)

    def __rsub__(self, other):
        # Non-commutative
        return Complex(other.re - self.re, other.im - self.im)


# if __name__ == '__main__':
#     a = Complex(2.0, 3.0)
#     b = Complex(-1.5, 2)
#     print(a + Complex(-1.5, 2))
#     print(a + 8)
#     print(3.5 + a)
#
#     c = Complex(1.0, -3.0)
#     print(c * Complex(4.0, 5.5))
#     print(c * 3.5)
#     print(-2 * c)
#
#     print(a / b)
#
#     print('1 + 6.0i', a - c)
#     print('-1.0 -6.0i', c - a)
