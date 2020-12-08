""" Solution to Day 07 of Advent of Code 2020 """
from pathlib import Path
import re
import typing as ty
import timeit
from collections import defaultdict

# Constants
DATA_PATH = Path.resolve(Path(__file__).parent)

with open(Path.joinpath(DATA_PATH, "input.txt")) as input_file:
    DATA = input_file.readlines()


# Data parsing functions
def get_data_rules(
    rules_list: ty.List[str],
) -> ty.Tuple[
    ty.DefaultDict[str, ty.List[str]], ty.DefaultDict[str, ty.List[ty.Tuple[int, str]]]
]:
    """Splits data into contained by and contains dicts

    Parameters
    ----------
    rules_list : list
        list of rules from input file

    Returns
    -------
    contaiend_in, contains : tuple
        dicts with lists of color ID's
    """
    contained_in, contains = defaultdict(list), defaultdict(list)
    for line in rules_list:
        split_line = line.split(" contain ")
        main_bag = split_line[0].replace(" bags", "")
        contained_bags = re.findall(r"(\d+) ([a-z ]+) [bag|bags,. ]+", split_line[1])

        for bag in contained_bags:
            number_bags, color = int(bag[0]), bag[1]
            contained_in[color].append(main_bag)
            contains[main_bag].append((number_bags, color))
    return contained_in, contains


# Data analysis
def get_colors_contained(
    col: str,
    contained_in: ty.DefaultDict[str, ty.List[ty.Tuple[int, str]]],
    color_dict: ty.Dict[str, bool],
) -> ty.Dict[str, bool]:
    """recursively find and store input color_dict

    Parameters
    ----------
    col : str
        bag color
    contained_in : DefaultDict
        contained_in from get_data_rules
    color_dict : DefaultDict
        empty default dict (initially), to be recursively filled

    Returns
    -------
    color_dict : dict
        color stings, bool key
    """
    for color in contained_in[col]:
        color_dict[color] = True
        if color in contained_in:
            get_colors_contained(color, contained_in, color_dict)
    return color_dict


def get_sum(
    col: str, contains: ty.DefaultDict[str, ty.List[ty.Tuple[int, str]]]
) -> int:
    """recursively gets sum of all bags contained within other bags

    Parameters
    ----------
    col : str
        bag color
    contains : DefaultDict
        contained from get_data_rules

    Returns
    -------
    sum_contained : int
        amount of bags contained within col bag
    """
    values = []
    for contained_bag in contains[col]:
        if contained_bag[1] in contains:
            values.append(contained_bag[0] * (get_sum(contained_bag[1], contains) + 1))
        else:
            values.append(contained_bag[0])
    return sum(values)


# Answers
PART_1_START_TIME = timeit.default_timer()
TARGET_KEY = "shiny gold"
BAGS_CONTAINING_SHINY_GOLD = {}  # storage dict - will be updated recursively
CONTAINED_IN, CONTAINS = get_data_rules(DATA)
BAGS_CONTAINING_SHINY_GOLD = get_colors_contained(
    TARGET_KEY, CONTAINED_IN, BAGS_CONTAINING_SHINY_GOLD
)
PART_1_ANS = len(BAGS_CONTAINING_SHINY_GOLD)
PART_1_TIME_MS = (timeit.default_timer() - PART_1_START_TIME) * 1000

PART_2_START_TIME = timeit.default_timer()
PART_2_ANS = get_sum(TARGET_KEY, CONTAINS)
PART_2_TIME_MS = (timeit.default_timer() - PART_2_START_TIME) * 1000

print(f"Part 1:\n{PART_1_ANS} 🧳 bags can contain 🥇 bag\n")
print(f"Part 2:\n{PART_2_ANS} 🧳 bags required in 🥇 bag\n")

print(
    f"Timed Results:\nPart 1: {PART_1_TIME_MS:.3f} ms\nPart 2: {PART_2_TIME_MS:.3f} ms\n"
)
