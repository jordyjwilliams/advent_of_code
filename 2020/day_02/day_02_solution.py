""" Solution to Day 02 of Advent of Code 2020 """
from pathlib import Path
import typing as ty

DATA_PATH = Path.resolve(Path(__file__).parent)
VALID_PASSWORDS_PART_1 = []
VALID_PASSWORDS_PART_2 = []

with open(Path.joinpath(DATA_PATH, "input.txt")) as input_file:
    DATA = input_file.readlines()


def split_line_of_file(input_line: str) -> ty.Tuple:
    """Splits string from input file.
    Returns tuple of password, substring, min_number, max_number
    """
    min_max_str, letter_str, password = input_line.replace("\n", "").split(" ")
    min_number, max_number = min_max_str.split("-")
    letter = letter_str.split(":")[0]
    return password, letter, int(min_number), int(max_number)


def password_is_valid_part_1(
    password: str, sub_string: str, min_number: int, max_number: int
) -> bool:
    """ Returns bool if password is valid for part 1 """
    num_occurrences = password.count(sub_string)
    return min_number <= num_occurrences <= max_number


def password_is_valid_part_2(
    password: str, sub_string: str, first_char_idx: int, second_char_idx: int
) -> bool:
    """Returns bool if password is valid for part 2
    Idx values are assumed to start at 0 (will be altered here)
    """
    first_char_val, second_char_val = (
        password[first_char_idx - 1],
        password[second_char_idx - 1],
    )
    return (first_char_val == sub_string) ^ (second_char_val == sub_string)


for line in DATA:
    line_data = split_line_of_file(line)
    if password_is_valid_part_1(*line_data):
        VALID_PASSWORDS_PART_1.append(line_data[0])
    if password_is_valid_part_2(*line_data):
        VALID_PASSWORDS_PART_2.append(line_data[0])

PART_1_ANS = len(VALID_PASSWORDS_PART_1)
print(f"Part 1:\n{PART_1_ANS} of {len(DATA)} passwords are valid\n")

PART_2_ANS = len(VALID_PASSWORDS_PART_2)
print(f"Part 2:\n{PART_2_ANS} of {len(DATA)} passwords are valid\n")
