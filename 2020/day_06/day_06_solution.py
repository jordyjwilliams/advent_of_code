""" Solution to Day 06 of Advent of Code 2020 """
from pathlib import Path
import timeit

# Constants
DATA_PATH = Path.resolve(Path(__file__).parent)

with open(Path.joinpath(DATA_PATH, "input.txt")) as input_file:
    DATA = input_file.read().strip()


# Data analysis functions
def group_count_yes_anyone(group_str: str) -> int:
    """Counts number of different questions answered yes by anyone in a group"""
    return len(set(group_str.replace("\n", "")))


def group_count_yes_everyone(group_str: str) -> int:
    """Counts number of different questions answered yes by everyone in a group"""
    group_size = len(group_str.split("\n"))
    combined_str = group_str.replace("\n", "")
    unique_chars = "".join(set(combined_str))
    return sum(
        [1 if combined_str.count(char) == group_size else 0 for char in unique_chars]
    )


# Answers
PART_1_START_TIME = timeit.default_timer()
GROUP_DATA = DATA.split("\n\n")
GROUP_YES_ANSWERS_ANYONE = [group_count_yes_anyone(group) for group in GROUP_DATA]
PART_1_ANS = sum(GROUP_YES_ANSWERS_ANYONE)
PART_1_TIME_MS = (timeit.default_timer() - PART_1_START_TIME) * 1000

PART_2_START_TIME = timeit.default_timer()
GROUP_YES_ANSWERS_EVERYONE = [group_count_yes_everyone(group) for group in GROUP_DATA]
PART_2_ANS = sum(GROUP_YES_ANSWERS_EVERYONE)
PART_2_TIME_MS = (timeit.default_timer() - PART_2_START_TIME) * 1000

print(f"Part 1:\n{PART_1_ANS} 👨‍👩‍👧‍👧 answered yes\n")
print(f"Part 2:\n{PART_2_ANS} 👨‍👩‍👧‍👧 answered yes\n")

print(
    f"Timed Results:\nPart 1: {PART_1_TIME_MS:.3f} ms\nPart 2: {PART_2_TIME_MS:.3f} ms\n"
)
