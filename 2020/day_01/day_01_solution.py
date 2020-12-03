""" Solution to Day 01 of Advent of Code 2020 """

from itertools import combinations
import typing as ty
from pathlib import Path
import numpy as np

DATA_PATH = Path.resolve(Path(__file__).parent)

with open(Path.joinpath(DATA_PATH, "input.txt")) as input_file:
    DATA = [int(x) for x in input_file.readlines()]


def get_numbers_that_sum(
    data: ty.List[int], numbers_that_sum: int = 2, target_sum: int = 2020
) -> ty.List[int]:
    """ Returns a list of numbers_that_sum which sum to target_sum """
    return [
        comb for comb in combinations(data, numbers_that_sum) if sum(comb) == target_sum
    ]


PART_1_INTS_TO_SUM = get_numbers_that_sum(DATA)
PART_1_ANS = [np.product(comb) for comb in PART_1_INTS_TO_SUM]

PART_2_INTS_TO_SUM = get_numbers_that_sum(DATA, 3)
PART_2_ANS = [np.product(comb) for comb in PART_2_INTS_TO_SUM]

print(f"Part 1:\nInts that sum are: {PART_1_INTS_TO_SUM}\nProduct is: {PART_1_ANS}\n")
print(f"Part 2:\nInts that sum are: {PART_2_INTS_TO_SUM}\nProduct is: {PART_2_ANS}\n")
