import pandas as pd
import numpy as np


class Die:
    """
    A class representing a single die with multiple faces and associated weights.

    Attributes:
    -----------
    die : pandas.DataFrame
        A dataframe holding the faces and weights of the die.
    """

    def __init__(self, faces):
        """
        Initialize the Die with a list or numpy array of unique faces.
        All weights are initialized to 1.0 by default.

        Parameters
        ----------
        faces : list or numpy.ndarray
            An array of unique face values for the die.

        Raises
        ------
        TypeError
            If faces is not a list or numpy array.
        ValueError
            If face values are not unique.
        """
        if not isinstance(faces, (list, np.ndarray)):
            raise TypeError("Faces must be a list or numpy array.")
        self.die = pd.DataFrame({'face': faces, 'weight': 1.0})

    def change_weight(self, face, new_weight):
        """
        Change the weight of a specific face of the die.

        Parameters
        ----------
        face : any
            The face whose weight is to be changed.
        new_weight : float or int
            The new weight value; must be numeric and non-negative.

        Raises
        ------
        ValueError
            If the face does not exist in the die.
        TypeError
            If new_weight is not numeric.
        """
        if face not in self.die['face'].values:
            raise ValueError(f"Face {face} does not exist.")
        self.die.loc[self.die['face'] == face, 'weight'] = new_weight

    def show_state(self):
        """
        Display the current state of the die including faces and weights.

        Returns
        -------
        pandas.DataFrame
            A DataFrame showing the current faces and corresponding weights.
        """
        return self.die

    def roll(self, num_rolls=1):
        """
        Simulate rolling the die a given number of times.

        Parameters
        ----------
        num_rolls : int, optional
            The number of times to roll the die (default is 1).

        Returns
        -------
        numpy.ndarray
            An array of face values resulting from the rolls.
        """
        outcomes = np.random.choice(
            self.die['face'],
            size=num_rolls,
            p=self.die['weight'] / self.die['weight'].sum()
        )
        return outcomes


class Game:
    """
    A class representing a game consisting of one or more dice of the same kind.

    Attributes
    ----------
    dice : list of Die
        A list containing Die objects used in the game.
    results : pandas.DataFrame or None
        DataFrame storing results from the most recent play. Initialized as None.
    """

    def __init__(self, dice):
        """
        Initialize the Game with a list of Die objects.

        Parameters
        ----------
        dice : list
            A list containing instances of the Die class.

        Raises
        ------
        TypeError
            If any object in the list is not an instance of Die.
        """
        if not isinstance(dice, list):
            raise TypeError("Dice must be a list of Die objects.")
        for die in dice:
            if not isinstance(die, Die):
                raise TypeError("All elements in the list must be Die objects.")
        self.dice = dice
        self._results = None

    def play(self, num_rolls):
        """
        Play the game by rolling all dice a specified number of times.

        Parameters
        ----------
        num_rolls : int
            The number of times to roll the dice.

        Returns
        -------
        None
            Results are stored in the 'results' attribute as a DataFrame.
        """
        outcomes = {}
        for i, die in enumerate(self.dice):
            outcomes[i] = die.roll(num_rolls)
        self._results = pd.DataFrame(outcomes)
        self._results.index.name = 'roll_number'

    def show_results(self, form='wide'):
        """
        Show the results of the most recent play.

        Parameters
        ----------
        form : str, optional
            Format of the output: 'wide' (default) for wide format,
            'narrow' for long format.

        Returns
        -------
        pandas.DataFrame
            A DataFrame of the play results in the specified format.

        Raises
        ------
        ValueError
            If form is not 'wide' or 'narrow'.
        """
        if self._results is None:
            raise ValueError("No results available. Please play the game first.")
        if form == 'wide':
            return self._results.copy()
        elif form == 'narrow':
            return self._results.melt(var_name='die_number', value_name='face_rolled', ignore_index=False)
        else:
            raise ValueError("Invalid form option. Use 'wide' or 'narrow'.")

class Analyzer:
    """
    A class to analyze results of a Game instance.

    Attributes
    ----------
    game : Game
        The Game object containing dice and results.
    results : pandas.DataFrame
        DataFrame storing the results of the game (faces rolled per die per roll).
    """

    def __init__(self, game):
        """
        Initialize the Analyzer with a Game instance.

        Parameters
        ----------
        game : Game
            The game instance whose results will be analyzed.

        Raises
        ------
        TypeError
            If the provided object is not an instance of Game.
        """
        if not isinstance(game, Game):
            raise TypeError("Input must be an instance of the Game class.")
        self.game = game
        self.results = game.show_results()

    def jackpot(self):
        """
        Compute the number of jackpots, i.e., rolls where all dice show the same face.

        Returns
        -------
        int
            The count of jackpots found in the game results.
        """
        return self.results[self.results.nunique(axis=1) == 1].shape[0]
    
    def face_counts_per_roll(self):
        """
        Count the number of times each face appears per roll.

        Returns
        -------
        pandas.DataFrame
            A DataFrame where each row corresponds to a roll and each column is a face.
            The cell values indicate how many times that face appeared in the roll.
        """
        return self.results.apply(lambda row: row.value_counts(), axis=1).fillna(0).astype(int)

    def combo(self):
        """
        Compute and return distinct combinations of faces rolled, along with their frequencies.

        Returns
        -------
        pandas.DataFrame
            DataFrame with columns 'combination' (a sorted tuple of faces) and 'count'.
            Each row represents a unique combination of faces and how often it occurred.
        """
        combos = self.results.apply(lambda row: tuple(sorted(row)), axis=1)
        return combos.value_counts().reset_index(name='count').rename(columns={'index': 'combination'})

    def permutation_count(self):
        """
        Compute how many times each face appears in each roll, preserving face order.

        Returns
        -------
        pandas.DataFrame
            DataFrame where each row represents a roll and each column is a face value.
            The cell values show how many times the face appeared in that roll.
        """
        return self.results.apply(lambda row: row.value_counts(), axis=1).fillna(0).astype(int)
