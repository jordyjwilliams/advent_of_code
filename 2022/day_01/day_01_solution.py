""" Solution to Day 01 of Advent of Code 2022 """

import timeit
import typing as ty
from pathlib import Path

DATA_PATH = Path.resolve(Path(__file__).parent)

with open(DATA_PATH / "input.txt", encoding="UTF-8") as input_file:
    DATA = input_file.read()


def parse_data_to_summation(
    data: str,
    delimiter: str = "",
) -> ty.List[int]:
    """Sum data, splitting list based on delimiter

    Parameters
    ----------
    data : str
        input data
    delimiter: str, optional
        delimiter to split summations around (default="")

    Returns
    -------
    summation : list[int]
        list of integers sum for each elf
    """
    summation = []
    elf_data = 0
    for line in data.split("\n"):
        if line != delimiter:
            elf_data += int(line)
        else:
            summation.append(elf_data)
            elf_data = 0
    return summation


PART_1_START_TIME = timeit.default_timer()
PART_1_ANS = max(parse_data_to_summation(DATA))
PART_1_TIME_MS = (timeit.default_timer() - PART_1_START_TIME) * 1000

PART_2_START_TIME = timeit.default_timer()
PART_2_ANS = sum(sorted(parse_data_to_summation(DATA), reverse=True)[0:3])
PART_2_TIME_MS = (timeit.default_timer() - PART_2_START_TIME) * 1000

if __name__ == "__main__":
    print(f"Part 1:\nMost calories carried by a singular elf: {PART_1_ANS} cal\n")
    print(f"Part 2:\nTop 3 elves are carrying a total of: {PART_2_ANS} cal\n")

    print(f"Timed Results:\n{PART_1_TIME_MS=:.3f}\n{PART_2_TIME_MS=:.3f}\n")
