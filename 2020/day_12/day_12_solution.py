""" Solution to Day 12 of Advent of Code 2020 """
import timeit
import typing as ty
from pathlib import Path

# Constants
DATA_PATH = Path.resolve(Path(__file__).parent)
# read data line by line
with open(DATA_PATH / "input.txt") as input_file:
    DATA = [(line[0], int(line[1:])) for line in input_file.readlines()]


# Part one
def run_path(instructions: ty.List[ty.Tuple[str, int]]) -> ty.Tuple[complex, complex]:
    """Runs instructions from a list of tuples

    Parameters
    ----------
    instructions : list
        list of operation (str) and amount (int) values

    Returns
    -------
    position : tuple
        of location and direction values

    Notes
    -----
    Assumes directions on the complex plane
    """
    # Use complex numbers as coord grid
    ## To get final position
    directions = {"N": 1j, "E": 1, "S": -1j, "W": -1}
    rotations = {"L": 1j, "R": -1j}
    location = 0
    direction = 1
    for operation, amount in instructions:
        if operation in directions:
            location += directions[operation] * amount
        elif operation in rotations:
            direction *= rotations[operation] ** (amount / 90)
        else:
            location += direction * amount
    return location, direction


def get_manhattan_distance(location: complex) -> int:
    """Gets Manhattan distance from complex location

    Parameters
    ----------
    location : complex
        direction in complex co-coordinateses

    Returns
    -------
    manhattan_distance : int

    Notes
    -----
    https://en.wikipedia.org/wiki/Taxicab_geometry
    """
    return int(abs(location.real) + abs(location.imag))


# Answers
PART_1_START_TIME = timeit.default_timer()
PART_1_LOCATION, PART_1_DIRECTION = run_path(DATA)
PART_1_ANS = get_manhattan_distance(PART_1_LOCATION)
PART_1_TIME_MS = (timeit.default_timer() - PART_1_START_TIME) * 1000

PART_2_START_TIME = timeit.default_timer()
PART_2_ANS = "CALCULATE THIS"
PART_2_TIME_MS = (timeit.default_timer() - PART_2_START_TIME) * 1000

if __name__ == "__main__":
    print(f"Part 1:\n{PART_1_ANS}\n")
    print(f"Part 2:\n{PART_2_ANS}\n")

    print(
        f"Timed Results:\nPart 1: {PART_1_TIME_MS:.3f} ms\nPart 2: {PART_2_TIME_MS:.3f} ms\n"
    )
