""" Solution to Day XX of Advent of Code 2022 """
import timeit
import typing as ty
from pathlib import Path

# Constants
DATA_PATH = Path.resolve(Path(__file__).parent)

# read data line by line
with open(DATA_PATH / "input.txt", encoding="UTF-8") as input_file:
    DATA = input_file.readlines()


def parse_dataline_to_bag_priority(data: str) -> ty.List[str]:
    """Priority for item which matches in both compartments of bag score for data line, returns list of integers.

    Parameters
    ----------
    data : str
        input data of bag contents. Each compartment is of equal length.

    Returns
    -------
    priorities : list[int]
        list of scores for each line
    """
    prio_map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    priorities = []
    for line in data:
        line = line.replace("\n", "")
        compartment1 = set(line[: len(line) // 2])
        compartment2 = set(line[len(line) // 2 :])
        priorities.append(prio_map.index((compartment1 & compartment2).pop()) + 1)
    return priorities


def parse_dataset_to_bag_priority(data: str) -> ty.List[str]:
    """Priority for item which matches over 3 lines in inputfile.

    Parameters
    ----------
    data : str
        input data of bag contents.

    Returns
    -------
    priorities : list[int]
        list of scores for each line
    """
    prio_map = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    priorities = []
    for idx in range(0, len(data), 3):
        bag_data = data[idx : idx + 3]
        bag_data = [line.replace("\n", "") for line in bag_data]
        bag1, bag2, bag3 = set(bag_data[0]), set(bag_data[1]), set(bag_data[2])
        priorities.append(prio_map.index((bag1 & bag2 & bag3).pop()) + 1)
    return priorities


# Answers
PART_1_START_TIME = timeit.default_timer()
PART_1_ANS = sum(parse_dataline_to_bag_priority(DATA))
PART_1_TIME_MS = (timeit.default_timer() - PART_1_START_TIME) * 1000

PART_2_START_TIME = timeit.default_timer()
PART_2_ANS = sum(parse_dataset_to_bag_priority(DATA))
PART_2_TIME_MS = (timeit.default_timer() - PART_2_START_TIME) * 1000

if __name__ == "__main__":
    print(f"{PART_1_ANS=}\n")
    print(f"{PART_2_ANS=}\n")

    print(f"Timed Results:\n{PART_1_TIME_MS=:.3f}\n{PART_2_TIME_MS=:.3f}\n")
