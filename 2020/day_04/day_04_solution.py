""" Solution to Day 04 of Advent of Code 2020 """
from pathlib import Path
import typing as ty
import timeit

# Constants
DATA_PATH = Path.resolve(Path(__file__).parent)
REQUIRED_KEYS = {"byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"}
OPTIONAL_KEYS = {"cid"}

with open(DATA_PATH / "input.txt") as input_file:
    DATA = input_file.read()

# Data splitting functions
def split_data_into_passports(data: ty.List[str]) -> ty.List[ty.Dict]:
    """Splits input data into dicts of passports

    Parameters
    ----------
    data : list
        list of strings of original passport data

    Returns
    -------
    parsed_data : list
        list of dict objects each dict contains:
            all data seperated by `:` object in file

    Notes
    -----
    Assumes:
    * Passports seperated by blank lines
    * Passport data seperated by space or new line
    * Passport data may not always be the same
        * will only be a subset of keys
    """
    passports_split = data.split("\n\n")
    passport_data = []
    for passport_str in passports_split:
        passport_dict = {}
        sub_string = passport_str.split()
        for key_val_pair in sub_string:
            key, val = key_val_pair.split(":")
            passport_dict[key] = val
        passport_data.append(passport_dict)
    return passport_data


# data checks for part 2
def check_year(input_year: str, min_year: int, max_year: int) -> bool:
    """Checks if a year is in a given range. Inclusive.

    Parameters
    ----------
    input_year : str
        string of input year (will be cast to int)
    min_year : int
        minimum year to be valid
    max_year : int
        maximum year to be valid

    Returns
    -------
    year_valid : bool
        if year in valid range
    """
    return min_year <= int(input_year) <= max_year


def check_height(input_height: str) -> bool:
    """Utility function to check height data from value.

    Parameters
    ----------
    input_height : str
        string of input height data

    Returns
    -------
    valid_height : bool
        if height in valid range

    Notes
    -----
    Assumes:
    * input is a string with a height seperated by a 2 digit unit
    * unit is either 'in' or 'cm'. Valid ranges are hardcoded
    """
    try:
        height, unit = int(input_height[:-2]), input_height[-2:]
    except ValueError:
        return False
    if unit == "cm":
        valid_height = 150 <= int(height) <= 193
    elif unit == "in":
        valid_height = 59 <= int(height) <= 76
    else:
        valid_height = False
    return valid_height


def check_hair_color(input_hair_color: str) -> bool:
    """Checks hair color against being valid hex

    Parameters
    ----------
    input_hair_color : str
        string hair_color to check validity of

    Returns
    -------
    valid_hair_color : bool
        if input_hair_color a valid string
    """
    if input_hair_color[0] != "#" or len(input_hair_color) != 7:
        return False
    try:
        int(input_hair_color[1:], 16)
        return True
    except ValueError:  # raised if cant convert hex values
        return False


def check_eye_color(input_eye_color: str, allowed_eye_colors: ty.List[str]) -> bool:
    """Utility function to check valid eye colors.
    Takes input eye color string and list of valid colors

    Parameters
    ----------
    input_eye_color : str
        eye color
    allowed_eye_colors : list
        list of allowed eye colors

    Returns
    -------
    valid_eye_color : bool
        if eye color in allowed eye_colors
    """
    return input_eye_color in allowed_eye_colors


def check_passport_id(input_pid: str) -> bool:
    """Checks passport id is a digit and 9 in len

    Parameters
    ----------
    input_pid : str
        passport ID from file

    Returns
    -------
    valid_passport_id : bool
        if valid
    """
    return input_pid.isdigit() and len(input_pid) == 9


# Constants for part 2 -> define checks
## key - data, value - callable
STRICTER_RULES_FUNCTIONS = {
    "byr": check_year,
    "iyr": check_year,
    "eyr": check_year,
    "hgt": check_height,
    "hcl": check_hair_color,
    "ecl": check_eye_color,
    "pid": check_passport_id,
    "cid": lambda x: True,  # can ignore, always valid
}

## List of function args, to be unpacked after the param value
STRICTER_RULES_ARGS = {
    "byr": [1920, 2002],
    "iyr": [2010, 2020],
    "eyr": [2020, 2030],
    "hgt": None,
    "hcl": None,
    "ecl": [["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]],
    "pid": None,
    "cid": None,
}

# Wrapper/validity functions
def valid_passport_part_1(passport_data: ty.Dict[str, ty.Any]) -> bool:
    """Checks if a passport dict is valid for part 1

    Parameters
    ----------
    passport_data : dict
        dict of passport data

    Returns
    -------
    valid_passport : bool
        if all required keys in passport
    """
    return passport_data.keys() >= REQUIRED_KEYS


def valid_passport_part_2(passport_data: ty.Dict[str, ty.Any]) -> bool:
    """Checks if a passport dict is valid for part 2

    Parameters
    ----------
    passport_data : dict
        dict of passport data

    Returns
    -------
    valid_passport : bool
        if valid for part 1 and keys pass criteria
    """
    valid_part_1 = valid_passport_part_1(passport_data)
    valid_data = {}
    if valid_part_1:
        for key, val in passport_data.items():
            if STRICTER_RULES_ARGS[key] is None:
                valid_data[key] = STRICTER_RULES_FUNCTIONS[key](val)
            else:
                valid_data[key] = STRICTER_RULES_FUNCTIONS[key](
                    val, *STRICTER_RULES_ARGS[key]
                )
        passport_valid = all(valid_data.values())
    else:
        passport_valid = False
    return passport_valid


# Answers
PART_1_START_TIME = timeit.default_timer()
DATA_IN_PASSPORTS = split_data_into_passports(DATA)
PART_1_ANS = sum([valid_passport_part_1(passport) for passport in DATA_IN_PASSPORTS])
PART_1_TIME_MS = (timeit.default_timer() - PART_1_START_TIME) * 1000

PART_2_START_TIME = timeit.default_timer()
PART_2_ANS = sum([valid_passport_part_2(passport) for passport in DATA_IN_PASSPORTS])
PART_2_TIME_MS = (timeit.default_timer() - PART_2_START_TIME) * 1000

print(f"Part 1:\n{PART_1_ANS} 🛂 valid passports\n")
print(f"Part 2:\n{PART_1_ANS} 🛂 valid passports\n")
print(
    f"Timed Results:\nPart 1: {PART_1_TIME_MS:.3f} ms\nPart 2: {PART_2_TIME_MS:.3f} ms\n"
)
