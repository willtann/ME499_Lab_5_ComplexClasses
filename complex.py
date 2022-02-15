#! /Users/tannerwilliams/Desktop/ME499/ME499_Lab_5_ComplexClasses/comlpex.py


class Complex:

    def __init__(self, re=0, im=0):
        self.re = float(re)
        self.im = float(im)

    def __repr__(self):
        return self.re

    def __str__(self):
        return self.im


if __name__ == '__main__':
    a = Complex(-3, 2)
    b = Complex(2)
    print(a.re, b.im)

    print(Complex())
