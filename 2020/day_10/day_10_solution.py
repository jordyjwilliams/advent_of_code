""" Solution to Day 10 of Advent of Code 2020 """
import collections
import timeit
from pathlib import Path

# Constants
DATA_PATH = Path.resolve(Path(__file__).parent)

# read data line by line
with open(DATA_PATH / "input.txt", encoding="UTF-8") as input_file:
    DATA = [int(line) for line in input_file.readlines()]


# Answers
PART_1_START_TIME = timeit.default_timer()

MAX_RATING = max(DATA) + 3
OUTLET_EFFECTIVE = 0
# Part one
DATA = [OUTLET_EFFECTIVE] + sorted(DATA) + [MAX_RATING]
DIFFERENCES = [DATA[i + 1] - val for i, val in enumerate(DATA[0:-1])]
COUNTED_DIFFS = collections.Counter(DIFFERENCES)

PART_1_ANS = COUNTED_DIFFS[1] * COUNTED_DIFFS[3]
PART_1_TIME_MS = (timeit.default_timer() - PART_1_START_TIME) * 1000


PART_2_START_TIME = timeit.default_timer()
# Dict of each key corresponding idx of each adapter, and num of paths to reach
NUM_PATH_COMBINATIONS = {0: 1}
for lower_idx, lower_val in enumerate(DATA):
    for upper_idx in range(lower_idx)[::-1]:
        if (lower_val - DATA[upper_idx]) <= 3:
            NUM_PATH_COMBINATIONS[lower_idx] = NUM_PATH_COMBINATIONS.get(
                lower_idx, 0
            ) + NUM_PATH_COMBINATIONS.get(upper_idx, 0)

PART_2_ANS = NUM_PATH_COMBINATIONS[len(DATA) - 1]  # Ignore final
PART_2_TIME_MS = (timeit.default_timer() - PART_2_START_TIME) * 1000

if __name__ == "__main__":
    print(f"{PART_1_ANS=} ⚡️ Jolts (1 Jolt * 3 Jolt)\n")
    print(f"{PART_2_ANS=} ⚡️ Combinations\n")

    print(f"Timed Results:\n{PART_1_TIME_MS=:.3f}\n{PART_2_TIME_MS=:.3f}\n")
