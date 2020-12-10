""" Solution to Day 01 of Advent of Code 2020 """

from itertools import combinations
import typing as ty
from pathlib import Path
import timeit
import numpy as np

DATA_PATH = Path.resolve(Path(__file__).parent)

with open(DATA_PATH / "input.txt") as input_file:
    DATA = [int(x) for x in input_file.readlines()]


def get_numbers_that_sum(
    data: ty.List[int], numbers_that_sum: int = 2, target_sum: int = 2020
) -> ty.List[int]:
    """Calculate a list of numbers which sum to target sum

    Parameters
    ----------
    data : list
        list of integers
    numbers_that_sum : int, optional
        how many numbers to sum, (default=2)
    target_sum : int, optional
        target sum of numbers, (default=2020)

    Returns
    -------
    numbers_summing_to_target : list
        list of tuples (of length numbers_that_sum)
        summing to target_sum
    """
    return [
        comb for comb in combinations(data, numbers_that_sum) if sum(comb) == target_sum
    ]


PART_1_START_TIME = timeit.default_timer()
PART_1_INTS_TO_SUM = get_numbers_that_sum(DATA)
PART_1_ANS = [np.product(comb) for comb in PART_1_INTS_TO_SUM]
PART_1_TIME_MS = (timeit.default_timer() - PART_1_START_TIME) * 1000

PART_2_START_TIME = timeit.default_timer()
PART_2_INTS_TO_SUM = get_numbers_that_sum(DATA, 3)
PART_2_ANS = [np.product(comb) for comb in PART_2_INTS_TO_SUM]
PART_2_TIME_MS = (timeit.default_timer() - PART_2_START_TIME) * 1000

if __name__ == "__main__":
    print(
        f"Part 1:\nInts that sum are: {PART_1_INTS_TO_SUM}\nProduct is: {PART_1_ANS}\n"
    )
    print(
        f"Part 2:\nInts that sum are: {PART_2_INTS_TO_SUM}\nProduct is: {PART_2_ANS}\n"
    )

    print(
        f"Timed Results:\nPart 1: {PART_1_TIME_MS:.3f} ms\nPart 2: {PART_2_TIME_MS:.3f} ms\n"
    )
