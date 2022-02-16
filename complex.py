#! /Users/tannerwilliams/Desktop/ME499/ME499_Lab_5_ComplexClasses/comlpex.py
from operator import __add__


class Complex:

    def __init__(self, re=0.0, im=0.0):
        # self.re = re
        # self.im = im
        self.re = re
        self.im = im

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        if self.im < 0:
            return '(' + self.re.__str__() + " " + '-' + " " + abs(self.im).__str__() + 'i' ')'
        else:
            return '(' + self.re.__str__() + " " + '+' + " " + abs(self.im).__str__() + 'i' ')'

    def __add__(self, other):
        if type(other) == int:
            other = float(other)

        # form ( complex + real )
        if type(other) == float:
            return Complex(self.re + other, self.im)

        # form ( complex + complex )
        else:
            return Complex(self.re + other.re, self.im + other.im)

    def __radd__(self, other):
        return self.__add__(other)

    # def __mul__(self, other):


if __name__ == '__main__':
    # a = Complex(2.0, 3.0)
    # b = Complex(-1.5, 2)
    # print(a + Complex(-1.5, 2)) # if of form ( x + (a + bi)) or ((a + bi) + x)
    # print(a + 8)
    # print(3.5 + a)








