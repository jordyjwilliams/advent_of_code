""" Solution to Day 05 of Advent of Code 2020 """
import timeit
import typing as ty
from pathlib import Path

# Constants
DATA_PATH = Path.resolve(Path(__file__).parent)
# use str values for string mapping
BINARY_MAPPING = {"F": "0", "B": "1", "L": "0", "R": "1"}
RANGES = {"row": 127, "column": 7}
ROW_DATA = ["F", "B"]
COL_DATA = ["R", "L"]

with open(DATA_PATH / "input.txt") as input_file:
    DATA = input_file.readlines()

# Data analysis functions - binary conversion
def get_row_and_column(seat_str: str) -> int:
    """Gets row and column from seat data is binary int

    Parameters
    ----------
    seat_str : str
        of format specified in challenge

    Returns
    -------
    binary_int : int
        binary int of mapped data
    """
    seat_str = seat_str.translate(str.maketrans(BINARY_MAPPING))
    return int(seat_str, 2)


def get_seat_id(all_ids: ty.List[int]) -> int:
    """Gets missing ID from list of all IDs
    Assumes only one missing number returns None no seat

    Parameters
    ----------
    all_ids : list
        list of input integers

    Returns
    -------
    assigned_seat_id : int
        seat_id from missing seat IDs
    """
    assigned_seat_id = None
    for seat_id in all_ids:
        # as all binary numbers until max range should exist (apart from very front)
        # numbers either side of current ID should exist, and not the one above
        target_id = seat_id + 1
        if target_id + 1 in all_ids and not target_id in all_ids:
            assigned_seat_id = target_id
            break
    return assigned_seat_id


# Answers
PART_1_START_TIME = timeit.default_timer()
ALL_SEAT_IDS = [get_row_and_column(seat) for seat in DATA]
PART_1_ANS = max(ALL_SEAT_IDS)
PART_1_TIME_MS = (timeit.default_timer() - PART_1_START_TIME) * 1000

PART_2_START_TIME = timeit.default_timer()
PART_2_ANS = get_seat_id(ALL_SEAT_IDS)
PART_2_TIME_MS = (timeit.default_timer() - PART_2_START_TIME) * 1000

if __name__ == "__main__":
    print(f"{PART_1_ANS=} 🛫 max seat number\n")
    print(f"{PART_2_ANS=} 🛫 seat ID\n")
    print(
        f"Timed Results:\n{PART_1_TIME_MS=:.3f}\n{PART_2_TIME_MS=:.3f}\n"
    )
