""" Solution to Day 14 of Advent of Code 2020 """
import timeit
from pathlib import Path

# Constants
DATA_PATH = Path.resolve(Path(__file__).parent)

# read data line by line
with open(DATA_PATH / "input.txt") as input_file:
    DATA = [line.strip() for line in input_file.readlines()]

# Answers
PART_1_START_TIME = timeit.default_timer()
MEMORY = {}
for line in DATA:
    split_line = line.split(" = ")
    if line[:4] == "mask":
        MASK = split_line[1]
    else:
        LOCATION = int(split_line[0].split("[")[1].replace("]", ""))
        VALUE = int(split_line[1])
        MEMORY_VALUES = list(bin(VALUE)[2:].zfill(len(MASK)))
        for mask_idx, mask_val in enumerate(MASK):
            if mask_val != "X":
                MEMORY_VALUES[mask_idx] = mask_val
            # Join all values, convert to binary int type
            VALUE = int("".join(MEMORY_VALUES), 2)
            MEMORY[LOCATION] = VALUE

PART_1_ANS = sum(MEMORY.values())
PART_1_TIME_MS = (timeit.default_timer() - PART_1_START_TIME) * 1000

PART_2_START_TIME = timeit.default_timer()
PART_2_ANS = "TODO"
PART_2_TIME_MS = (timeit.default_timer() - PART_2_START_TIME) * 1000

if __name__ == "__main__":
    print(f"{PART_1_ANS=}\n")
    print(f"{PART_2_ANS=}\n")

    print(f"Timed Results:\n{PART_1_TIME_MS=:.3f}\n{PART_2_TIME_MS:.3f}\n")
