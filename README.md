# Monte Carlo Simulator

## Metadata
- **Name:** Didier Kasole
- **Net ID:** xbw8de
- **Course:** DS 5100
- **Date:** 29 April 2025
- **Description:**  
  This simulator rolls customizable letter dice, stores the outcomes, and analyzes permutations to identify valid words.

---

## Synopsis

Example usage of the module:

```python
from montecarlo import Die, Game, Analyzer

# Die class
die = Die([1, 2, 3])
die.change_weight(1, 5)
print(die.show_state())

# Game class
die1 = Die([1, 2, 3])
die2 = Die([1, 2, 3])
game = Game([die1, die2])
game.play(10)
print(game.show_results())

# Analyzer class
die = Die([1, 2, 3])
game = Game([die])
game.play(5)
analyzer = Analyzer(game)
jackpot_count = analyzer.jackpot()
print(game.show_results())
```

---

## API Description

### Die Class
Represents a single die that can be rolled. Each face can have a custom weight.

- `Die(faces)`: Create a die with a list of faces.
- `change_weight(face, new_weight)`: Change the weight of a given face.
- `roll_die()`: Roll the die once.
- `show_state()`: Show current faces and weights as a DataFrame.

Example:

```python
die = Die([1, 2, 3])
die.change_weight(1, 5)
print(die.show_state())
```

### Game Class
Represents a game consisting of rolling one or more dice together.

- `Game(dice)`: Create a game with a list of `Die` objects.
- `play(num_rolls)`: Roll all dice a specified number of times.
- `show_results(form='wide')`: Show the results in wide or narrow format.

Example:

```python
die1 = Die([1, 2, 3])
die2 = Die([1, 2, 3])
game = Game([die1, die2])
game.play(10)
print(game.show_results())
```

### Analyzer Class
Analyzes a completed game for certain patterns.

- `Analyzer(game)`: Create an analyzer from a `Game` object.
- `jackpot()`: Counts the number of jackpots (rolls where all faces match).
- `combo()`: Identifies all distinct combinations rolled.
- `face_counts_per_roll()`: Calculates how often each face appears per roll.

Example:

```python
die = Die([1, 2, 3])
game = Game([die])
game.play(5)
analyzer = Analyzer(game)
jackpot_count = analyzer.jackpot()
print(jackpot_count)
```

---

## Notes
- Ensure `numpy`, `pandas`, `itertools`, and `matplotlib` are installed.
- Developed and tested for educational purposes in DS 5100 Spring 2025.


