#! /Users/tannerwilliams/Desktop/ME499/ME499_Lab_5_ComplexClasses/comlpex.py


class Complex:

    def __init__(self, re=0, im=0):
        self.re = float(re)
        self.im = float(im)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        if self.im < 0:
            return '(' + self.re.__str__() + " " + '-' + " " + abs(self.im).__str__() + 'i' ')'
        else:
            return '(' + self.re.__str__() + " " + '+' + " " + abs(self.im).__str__() + 'i' ')'

    def __add__(self, complex_1):
        # if complex_1
        net.re = complex_1.re + complex_2.im
        net.im = complex_1.re + complex_2.im
        return net.__repr__()

    def __radd__(self, complex_1, complex_2):
        return self.__add__(complex_1, complex_2)

if __name__ == '__main__':
    # a = Complex(-3, 2)
    # b = Complex(2)
    # print(a.re, b.im)
    #
    # print(Complex(3.4, -2.1))
    # print(Complex(-3.0, 2))

    a = Complex(2.0, 3.0)
    print(a + Complex(-1.5, 2))
    print(type(a))



