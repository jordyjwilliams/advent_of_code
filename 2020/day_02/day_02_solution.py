""" Solution to Day 02 of Advent of Code 2020 """
from pathlib import Path
import timeit
import typing as ty

DATA_PATH = Path.resolve(Path(__file__).parent)
VALID_PASSWORDS_PART_1 = []
VALID_PASSWORDS_PART_2 = []

with open(Path.joinpath(DATA_PATH, "input.txt")) as input_file:
    DATA = input_file.readlines()


def split_line_of_file(input_line: str) -> ty.Tuple[str, str, int, int]:
    """Splits string from input file.

    Parameters
    -----------
    input_line : str
        line from input data

    Returns
    -------
    data : tuple
        password, letter, min_number, max_number
    """
    min_max_str, letter_str, password = input_line.replace("\n", "").split(" ")
    min_number, max_number = min_max_str.split("-")
    letter = letter_str.split(":")[0]
    return password, letter, int(min_number), int(max_number)


def password_is_valid_part_1(
    password: str, sub_string: str, min_number: int, max_number: int
) -> bool:
    """Checks if password is valid for part 1 criteria

    Parameters
    ----------
    password : str
        password to check
    sub_string : str
        letter or substring which must be in password
    min_number : int
        minimum number of times sub_string must occur
    max_number : int
        maximmum number of times sub_string can occur

    Returns
    -------
    valid : bool
        if password is valid
    """
    num_occurrences = password.count(sub_string)
    return min_number <= num_occurrences <= max_number


def password_is_valid_part_2(
    password: str, sub_string: str, first_char_idx: int, second_char_idx: int
) -> bool:
    """Returns bool if password is valid for part 2

    Parameters
    ----------
    password : str
        password to check
    sub_string : str
        letter or substring which must be in password
    first_char_idx : int
        position where sub_string must occur once
    second_char_idx : int
        position where sub_string must occur once

    Returns
    -------
    valid : bool
        if password is valid

    Notes
    -----
    * Index values are assumed to start at 0 (will be altered here)
    * Substring must only occur once at first_char_idx or second_char_idx
    """
    first_char_val, second_char_val = (
        password[first_char_idx - 1],
        password[second_char_idx - 1],
    )
    return (first_char_val == sub_string) ^ (second_char_val == sub_string)


START_TIME = timeit.default_timer()
for line in DATA:
    line_data = split_line_of_file(line)
    if password_is_valid_part_1(*line_data):
        VALID_PASSWORDS_PART_1.append(line_data[0])
    if password_is_valid_part_2(*line_data):
        VALID_PASSWORDS_PART_2.append(line_data[0])

PART_1_ANS = len(VALID_PASSWORDS_PART_1)
PART_2_ANS = len(VALID_PASSWORDS_PART_2)

END_TIME_MS = (timeit.default_timer() - START_TIME) * 1000


print(f"Part 1:\n{PART_1_ANS} of {len(DATA)} passwords are valid\n")
print(f"Part 2:\n{PART_2_ANS} of {len(DATA)} passwords are valid\n")
print(f"Timed Results:\nParts 1 & 2: {END_TIME_MS} ms\n")
