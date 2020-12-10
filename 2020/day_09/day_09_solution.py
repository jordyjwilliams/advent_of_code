""" Solution to Day 09 of Advent of Code 2020 """
import timeit
import typing as ty
from itertools import combinations
from pathlib import Path

# Constants
DATA_PATH = Path.resolve(Path(__file__).parent)
PREAMBLE_LENGTH = 25

# read data line by line
with open(DATA_PATH / "input.txt") as input_file:
    DATA = [int(x) for x in input_file.readlines()]


def is_valid(current_input: int, previous_numbers: ty.List[int]):
    """Checks if input is valid depending on a previous numbers

    Parameters
    ----------
    current_input : int
        current input value to check
    previous_numbers : list
        of integers of previous input values

    Returns
    -------
    number_valid : bool
        if a combination of 2 (or more) previous numbers sums to
        current input
    """
    numbers_that_sum = [
        comb for comb in combinations(previous_numbers, 2) if sum(comb) == current_input
    ]
    return bool(numbers_that_sum)


# Answers
PART_1_START_TIME = timeit.default_timer()

for idx, val in enumerate(DATA):
    if idx < PREAMBLE_LENGTH:
        continue
    if not is_valid(val, DATA[idx - PREAMBLE_LENGTH : idx]):
        PART_1_ANS, PART_1_IDX = val, idx
        break

PART_1_TIME_MS = (timeit.default_timer() - PART_1_START_TIME) * 1000

PART_2_START_TIME = timeit.default_timer()

DATA_BEFORE_PART_1_ANS = DATA[:PART_1_IDX]
for search_size in range(2, len(DATA_BEFORE_PART_1_ANS)):
    for idx, _ in enumerate(DATA_BEFORE_PART_1_ANS[:-search_size]):
        DATA_RANGE = DATA_BEFORE_PART_1_ANS[idx : idx + search_size]
        if sum(DATA_RANGE) != PART_1_ANS:
            continue
        PART_2_LIST = DATA_RANGE
        break

PART_2_ANS = min(PART_2_LIST) + max(PART_2_LIST)
PART_2_TIME_MS = (timeit.default_timer() - PART_2_START_TIME) * 1000

if __name__ == "__main__":
    print(f"Part 1:\n{PART_1_ANS} not valid at {PART_1_IDX}\n")
    print(
        f"Part 2:\n{PART_2_ANS} is the sum of the contiguous range of {len(PART_2_LIST)} numbers\n"
    )

    print(
        f"Timed Results:\nPart 1: {PART_1_TIME_MS:.3f} ms\nPart 2: {PART_2_TIME_MS:.3f} ms\n"
    )
