""" Solution to Day 06 of Advent of Code 2022 """
import timeit
from pathlib import Path

# Constants
DATA_PATH = Path.resolve(Path(__file__).parent)

# read data line by line
with open(DATA_PATH / "input.txt", encoding="UTF-8") as input_file:
    DATA = input_file.read()


def parse_data_to_unique(data: str, buffer_number: int) -> int:
    """Parses data as a whole string.
    Searches over the string for the idx where a unique `buffer_number` of chars exists.

    Parameters
    ----------
    data : str
        datastream buffer string
    buffer_number : int
        buffer number to search over

    Returns
    -------
    idx_unique_buffer : int
        idx where unique `buffer_number` first exists.
    """
    for idx, _ in enumerate(data):
        if len(set(data[idx : idx + buffer_number])) == buffer_number:
            return idx + buffer_number
    return None


# Answers
PART_1_START_TIME = timeit.default_timer()
PART_1_ANS = parse_data_to_unique(DATA, buffer_number=4)
PART_1_TIME_MS = (timeit.default_timer() - PART_1_START_TIME) * 1000

PART_2_START_TIME = timeit.default_timer()
PART_2_ANS = parse_data_to_unique(DATA, buffer_number=14)
PART_2_TIME_MS = (timeit.default_timer() - PART_2_START_TIME) * 1000

if __name__ == "__main__":
    print(f"{PART_1_ANS=}\n")
    print(f"{PART_2_ANS=}\n")

    print(f"Timed Results:\n{PART_1_TIME_MS=:.3f}\n{PART_2_TIME_MS=:.3f}\n")
