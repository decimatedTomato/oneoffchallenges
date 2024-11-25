"""
Istanbul Tea House rules:
Announce a number between 3 and 12. Then roll both dice.
If you roll equal to or greater than the announced
number, take the announced number of Lira from the
general supply. Otherwise, only take 2 Lira.
"""

from itertools import product
from pprint import pformat
from math import isclose

likelihoods = {
    2:  1/36,
    3:  2/36,
    4:  3/36,
    5:  4/36,
    6:  5/36,
    7:  6/36,
    8:  5/36,
    9:  4/36,
    10: 3/36,
    11: 2/36,
    12: 1/36,
}
cumulative_likelihoods = {
    2: 36/36,
    3: 35/36,
    4: 33/36,
    5: 30/36,
    6: 26/36,
    7: 21/36,
    8: 15/36,
    9: 10/36,
    10: 6/36,
    11: 3/36,
    12: 1/36,
}

def evaluate(guess, roll):
    return guess if roll >= guess else 2

def expected_value(guess):
    return sum(evaluate(guess, roll) * likelihoods[roll] for roll in range(2, 13))

EVs = {guess: expected_value(guess) for guess in range(3, 13)}
EV_max = max(EVs.values())
guesses_max = [guess for guess in EVs if isclose(EVs[guess], max(EVs.values()))]
print("Standard odds:")
print(f"The expected values of guesses are \n{pformat(EVs, 1)}.")
print(f"Therefore the highest expected value is {EV_max}.")
print(f"The guesse(s) that have this expected value are {guesses_max}.")

"""
If you have the red Mosque tile, you may turn one
die to “4” after the roll or re-roll both dice.
"""

def upgraded_evaluate(guess, d1, d2):
    if d1 + d2 >= guess: return guess
    if 4 + max(d1, d2) >= guess: return guess
    return expected_value(guess)

def upgraded_expected_value(guess):
    rolls = [(i, j) for i in range(1, 7) for j in range(1, 7)]
    return sum(upgraded_evaluate(guess, d1, d2) for (d1, d2) in rolls) / 36

upgraded_EVs = {guess: upgraded_expected_value(guess) for guess in range(3, 13)}
upgraded_EV_max = max(upgraded_EVs.values())
upgraded_guesses_max = [guess for guess in upgraded_EVs if isclose(upgraded_EVs[guess], max(upgraded_EVs.values()))]
print("After acquiring red mosque tile:")
print(f"The expected values of guesses are \n{pformat(upgraded_EVs, 1)}.")
print(f"Therefore the highest expected value is {upgraded_EV_max}.")
print(f"The guesse(s) that have this expected value are {upgraded_guesses_max}.")