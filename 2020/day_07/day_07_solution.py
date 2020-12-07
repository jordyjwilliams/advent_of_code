""" Solution to Day 07 of Advent of Code 2020 """
from pathlib import Path
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
) -> ty.Tuple[ty.DefaultDict, ty.DefaultDict]:
    """splits data into contained by and contains dicts"""
    contained_in, contains = defaultdict(list), defaultdict(list)
    for line in rules_list:
        split_line = line.split(" contain ")
        main_bag = split_line[0].replace(" bags", "")
        parts = (
            split_line[1]
            .replace(" bags", "")
            .replace(" bag", "")
            .replace(".", "")
            .split(",")
        )
        for bag in parts:
            bag = bag.strip()
            if bag[0].isdigit():
                number_bags, color = int(bag[0]), bag[2:]
            else:
                number_bags, color = 0, None
            contained_in[color].append(main_bag)
            contains[main_bag].append((number_bags, color))
    return contained_in, contains


# Data analysis
def get_colors_contained(
    col: str, contained_in: ty.List, color_dict: ty.DefaultDict[str, bool]
) -> ty.DefaultDict[str, bool]:
    """recursively find and store input color_dict
    color_dict should initially be empty dict
    """
    for color in contained_in[col]:
        color_dict[color] = True
        if color in contained_in:
            get_colors_contained(color, contained_in, color_dict)
    return color_dict


def get_sum(
    col: str, contains: ty.DefaultDict[str, ty.List[ty.Tuple[int, str]]]
) -> int:
    """ recursively gets sum of all bags contained within other bags """
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
