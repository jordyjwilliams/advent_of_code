""" Solution to Day 03 of Advent of Code 2020 """
from pathlib import Path
import typing as ty
import timeit
import numpy as np

DATA_PATH = Path.resolve(Path(__file__).parent)

""" Slopes to check --> PART 2
    Right 1, down 1.
    Right 3, down 1. Part 1
    Right 5, down 1.
    Right 7, down 1.
    Right 1, down 2.
"""

PART_2_SLOPES = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]

with open(DATA_PATH / "input.txt") as input_file:
    DATA = [
        line.strip() for line in input_file.readlines()
    ]  # each line will be one 'row' of map


def count_number_trees_hit_in_path(
    data: ty.List, num_right: int = 3, num_down: int = 1
) -> int:
    """Counts number of trees hit in a traverse path.

    Parameters
    ----------
    data : list
        list of strings containing terrain data
    num_right : int, optional
        how many indices to move right each step, (default=3)
    num_down : int, optional
        how many indices to move down each step, (default=1)

    Returns
    -------
    num_trees_hit : int
        how many times tree occurred in path

    Notes
    -----
    Assumes:
    * all rows loop
    * tree is # symbol
    """
    # Define start position in top left
    right_start = down_start = num_trees = 0
    while down_start < len(data):
        num_trees += data[down_start][right_start % len(data[0])] == "#"
        right_start += num_right
        down_start += num_down
    return num_trees


PART_1_START_TIME = timeit.default_timer()
PART_1_ANS = count_number_trees_hit_in_path(DATA)
PART_1_TIME_MS = (timeit.default_timer() - PART_1_START_TIME) * 1000

PART_2_START_TIME = timeit.default_timer()
PART_2_PER_SLOPE = [
    count_number_trees_hit_in_path(DATA, slope[0], slope[1]) for slope in PART_2_SLOPES
]
PART_2_ANS = np.product(PART_2_PER_SLOPE)
PART_2_TIME_MS = (timeit.default_timer() - PART_2_START_TIME) * 1000

print(f"Part 1:\n{PART_1_ANS} 🎄 hit\n")
print(f"Part 2:\n{PART_2_PER_SLOPE} 🎄 hit for {PART_2_SLOPES}")
print(f"Answer: {PART_2_ANS}\n")
print(
    f"Timed Results:\nPart 1: {PART_1_TIME_MS:.3f} ms\nPart 2: {PART_2_TIME_MS:.3f} ms\n"
)
