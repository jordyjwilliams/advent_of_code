""" Solution to Day XX of Advent of Code 2020 """
import timeit
from pathlib import Path

# Constants
DATA_PATH = Path.resolve(Path(__file__).parent)

# read data line by line
with open(DATA_PATH / "input.txt") as input_file:
    DATA = input_file.readlines()


# Data parsing functions
# DEFINE HERE...


# Data analysis
# DEFINE HERE...

# Answers
PART_1_START_TIME = timeit.default_timer()
PART_1_ANS = "TODO"
PART_1_TIME_MS = (timeit.default_timer() - PART_1_START_TIME) * 1000

PART_2_START_TIME = timeit.default_timer()
PART_2_ANS = "TODO"
PART_2_TIME_MS = (timeit.default_timer() - PART_2_START_TIME) * 1000

if __name__ == "__main__":
    print(f"{PART_1_ANS=}\n")
    print(f"{PART_2_ANS=}\n")

    print(f"Timed Results:\n{PART_1_TIME_MS=:.3f}\n{PART_2_TIME_MS=:.3f}\n")
