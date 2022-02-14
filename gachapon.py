#! /Users/tannerwilliams/Desktop/ME499/ME499_Lab_5_ComplexClasses/gachapon.py


class GachaponSimulator:

    # Initialize attribute: size of prize pool
    def __init__(self, prizes_n):
        self.prizes_n = prizes_n


if __name__ == '__main__':
    game = GachaponSimulator(5)
    print(game.prizes_n)