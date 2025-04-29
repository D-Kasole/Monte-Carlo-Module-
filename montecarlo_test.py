import unittest
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from montecarlo import Die, Game, Analyzer
import itertools
help(Die)
help(Game)
help(Analyzer)



class TestDie(unittest.TestCase):
    def test_change_weight(self):
        die = Die([1, 2, 3])
        die.change_weight(1, 5)
        print(die.show_state()) 
        self.assertEqual(die.show_state().loc[0, 'weight'], 5)

class TestGame(unittest.TestCase):
    def test_play(self):
        die1 = Die([1, 2, 3])
        die2 = Die([1, 2, 3])
        game = Game([die1, die2])
        game.play(10)
        self.assertEqual(len(game.show_results()), 10)

class TesttAnalyzer(unittest.TestCase):
    def test_jackpot(self):
        die = Die([1, 2, 3])
        game = Game([die])
        game.play(5)
        analyzer = Analyzer(game)
        jackpot_count = analyzer.jackpot()
        print(game.show_results()) 
        self.assertIsInstance(jackpot_count, int)

if __name__ == '__main__':
    unittest.main()