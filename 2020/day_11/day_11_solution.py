""" Solution to Day 11 of Advent of Code 2020 """
import itertools
import timeit
import typing as ty
from copy import deepcopy
from pathlib import Path

# Constants
DATA_PATH = Path.resolve(Path(__file__).parent)

# read data line by line
with open(DATA_PATH / "input.txt") as input_file:
    # Pad rows with "." floor charecters
    DATA = ["@" + line.strip() + "@" for line in input_file]

# Pad columns with "." floor charecters
## No overlap/out of bounds check needed.
PAD_COL = ["@" * len(DATA[0])]
DATA = PAD_COL + DATA + PAD_COL


def number_occupied(
    seat_lines: ty.List[str], current_row_idx: int, current_col_idx: int
) -> int:
    """Calculates the number of occupied seats in a grid surrounding a current position

    Parameters
    ----------
    seat_lines : list
        list of strings of rows
    current_row_idx : int
        index of the current row position
    current_col_idx : int
        index of the current column position

    Returns
    -------
    number_occupied_seats : int
        Number of "#" instances

    Notes
    -----
    * seat_lines grid data must be padded.
    * eg will not check out of bound for a 3x3 grid.
    * assumes 3x3 search size
    * number of instances includes the current position
    """
    row_search_idx = current_row_idx - 1, current_row_idx + 2
    col_search_idx = current_col_idx - 1, current_col_idx + 2
    row_search_data = seat_lines[row_search_idx[0] : row_search_idx[1]]
    return sum(
        [
            col[col_search_idx[0] : col_search_idx[1]].count("#")
            for col in row_search_data
        ]
    )


def first_occupied(
    seat_lines: ty.List[str], current_row_idx: int, current_col_idx: int
) -> int:
    """Counts number of first occupied seats

    Parameters
    ----------
    seat_lines : list
        list of strings of rows
    current_row_idx : int
        index of the current row position
    current_col_idx : int
        index of the current column position

    Returns
    -------
    number_occupied_seats : int
        Number of "#" instances

    Notes
    -----
    Does nothing for '.' empty seats
    Includes initial seat in the occupied count
    """
    total_occupied = 0
    for row_direction, col_direction in itertools.product((-1, 0, 1), repeat=2):
        for search_range in itertools.count(1):
            search_seat = seat_lines[current_row_idx + search_range * row_direction][
                current_col_idx + search_range * col_direction
            ]
            if search_seat != ".":  # don't want to break unless not missing seat
                total_occupied += 1 if search_seat == "#" else 0
                break
    return total_occupied


def replace_str_at_idx(input_str: str, idx: int, replacement: str) -> str:
    """Replaces the given index of a string with replacement str

    Parameters
    ----------
    input_str : str
        input string to modify
    idx : int
        index to change
    replacement : str

    Returns
    -------
    replaced_str : str
        input_str with replacement added at idx
    """
    return input_str[:idx] + replacement + input_str[idx + 1 :]


def run_equilibrium_state(
    seat_lines: ty.List[str], number_needed_to_vacate: int, first_visible: bool
) -> ty.List[str]:
    """Gets equilibrium position of seats

    Parameters
    ----------
    seat_lines : list
        list of strings of rows
    number_needed_to_vacate : int
        number of surrounding seats that need to be occupied
        for somone to vacate (inclusive)
    first_visible : bool
        if the equilibrium state should be reached by first visible seats (Part 2)
        if False, surrounding seats used

    Return
    ------
    equilibrium_lines : list
        of seats in equilibrium
    """
    previous_seats = None
    seat_lines = deepcopy(seat_lines)  # copy object to avoid input modification
    callable_counter = first_occupied if first_visible else number_occupied
    while previous_seats != seat_lines:
        previous_seats = deepcopy(seat_lines)
        for current_row_idx, current_row_val in enumerate(previous_seats):
            for current_col_idx, current_seat in enumerate(current_row_val):
                if current_seat in ".@":  # include buffer char
                    continue
                num_occupied_seats = callable_counter(
                    previous_seats, current_row_idx, current_col_idx
                )
                if current_seat == "L" and num_occupied_seats == 0:
                    seat_lines[current_row_idx] = replace_str_at_idx(
                        seat_lines[current_row_idx], current_col_idx, "#"
                    )
                elif (
                    current_seat == "#"
                    and num_occupied_seats - 1 >= number_needed_to_vacate
                ):  # remove the center idx
                    seat_lines[current_row_idx] = replace_str_at_idx(
                        seat_lines[current_row_idx], current_col_idx, "L"
                    )
    return seat_lines


# Answers
PART_1_START_TIME = timeit.default_timer()
PART_1_ANS = sum(
    line.count("#")
    for line in run_equilibrium_state(
        DATA, number_needed_to_vacate=4, first_visible=False
    )
)
PART_1_TIME_MS = (timeit.default_timer() - PART_1_START_TIME) * 1000


PART_2_START_TIME = timeit.default_timer()
PART_2_ANS = sum(
    line.count("#")
    for line in run_equilibrium_state(
        DATA, number_needed_to_vacate=5, first_visible=True
    )
)
PART_2_TIME_MS = (timeit.default_timer() - PART_2_START_TIME) * 1000

if __name__ == "__main__":
    print(f"Part 1:\n{PART_1_ANS}\n")
    print(f"Part 2:\n{PART_2_ANS}\n")

    print(
        f"Timed Results:\nPart 1: {PART_1_TIME_MS:.3f} ms\nPart 2: {PART_2_TIME_MS:.3f} ms\n"
    )
