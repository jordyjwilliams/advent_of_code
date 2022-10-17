""" Solution to Day 13 of Advent of Code 2020 """
import itertools
import timeit
from pathlib import Path

from sympy.ntheory.modular import solve_congruence  # pylint:disable=E0401

# Constants
DATA_PATH = Path.resolve(Path(__file__).parent)

# read data line by line
with open(DATA_PATH / "input.txt", encoding="UTF-8") as input_file:
    DATA = input_file.readlines()

# Answers
PART_1_START_TIME = timeit.default_timer()

EARLIEST_TIME = int(DATA[0])

# -ve idx needed for sypmy solve_congruence
BUS_IDX_IDS = [
    (-idx, int(bus)) for idx, bus in enumerate(DATA[1].split(",")) if bus != "x"
]

SORTED_BUS_IDS = sorted([idx_bus[1] for idx_bus in BUS_IDX_IDS])

for bus in SORTED_BUS_IDS:  # idx not necessary for part 1
    for minute in itertools.count(EARLIEST_TIME):
        if minute % bus == 0:
            BUS_TIMESTAMP = minute
            EARLIEST_BUS_ID = bus
            break

WAIT_TIME = BUS_TIMESTAMP - EARLIEST_TIME
# Bus ID * num of mins to wait
PART_1_ANS = EARLIEST_BUS_ID * WAIT_TIME
PART_1_TIME_MS = (timeit.default_timer() - PART_1_START_TIME) * 1000

PART_2_START_TIME = timeit.default_timer()
PART_2_ANS = solve_congruence(*BUS_IDX_IDS)[0]
PART_2_TIME_MS = (timeit.default_timer() - PART_2_START_TIME) * 1000

if __name__ == "__main__":
    print(f"{PART_1_ANS=} 🚌. Could take {EARLIEST_BUS_ID=} at {EARLIEST_TIME=}\n")
    print(f"{PART_2_ANS=} 🚌⌚︎\n")

    print(f"Timed Results:\n{PART_1_TIME_MS=:.3f}\n{PART_2_TIME_MS=:.3f}\n")
