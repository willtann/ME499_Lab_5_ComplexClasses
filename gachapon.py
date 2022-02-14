#! /Users/tannerwilliams/Desktop/ME499/ME499_Lab_5_ComplexClasses/gachapon.py
import random
import numpy as np
import sys

class GachaponSimulator:

    # Initialize attribute: size of prize pool
    def __init__(self, n_prizes):
        self.n_prizes = n_prizes  # attribute - number of prizes in a pool
        self.results = []  # attribute- empty list for results

    def _simulate_once(self):
        # Initialize a dictionary with a prize count of zero
        prize_pool = list(range(0, self.n_prizes))
        # print('_simulate_once/prize_pool = ', prize_pool)
        scorecard = {}
        for prize_num in prize_pool:
            scorecard[prize_num] = 0

        # Empty list to keep a running tally of prizes
        my_prizes = []
        # Keep looping while there are any prizes with a count of 0
        while min(scorecard.values()) < 1:
            # Draw a random number from possible prize range
            draw = random.choice(prize_pool)
            # Add new prize to current prizes
            my_prizes.append(draw)
            # Add new prize to count of that same prize
            for key in prize_pool:
                if draw == key:
                    scorecard[key] += 1
        else:  # If all prizes have been won
            # print('_simulate_once/my_prizes = ', my_prizes)
            # print('_simulate_once/len(my_prizes) = ', len(my_prizes))
            return len(my_prizes)

    def reset(self):
        self.results = []

    def simulate(self, num_games):
        for game in range(0, num_games):
            self.results.append(self._simulate_once())
        return self.results

    def get_summary_results(self):
        if len(self.results) == 0:
            mean = None
            stdev = None
        elif len(self.results) < 2:
            mean = np.mean(self.results)
            stdev = None
        else:
            mean = np.mean(self.results)
            stdev = np.std(self.results)

        summary = {"n": len(self.results), "mean": mean, "stdev": stdev}
        return summary


if __name__ == '__main__':
  # Make sure two arguments are provided
    if not (sys.argv[1:]):
        raise Exception('Need two arguments ...')
    else:
        for arg in sys.argv[1:]:
            # Getting sentiment.txt for scoring
            scoring_dict = load_score_dict()
            # Open and convert the file from user to a string
            mytext = str(list(open(arg)))
            # Score text according to the scoring dictionary
            # 1. Turn string of text into a list of words without any punctuation or capitalization
            # 2. Go through each word and apply scoring
            # 3. Sum scores for given .txt
            score = score_sentence(mytext, scoring_dict)
