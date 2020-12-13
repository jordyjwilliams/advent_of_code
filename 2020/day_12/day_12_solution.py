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
def run_path(
    instructions: ty.List[ty.Tuple[str, int]], start_waypoint: complex = None
) -> ty.Tuple[complex, complex]:
    """Runs instructions from a list of tuples

    Parameters
    ----------
    instructions : list
        list of operation (str) and amount (int) values
    start_waypoint : complex, optional
        starting waypoint, default=None (Part 1)

    Returns
    -------
    position : tuple
        of location and waypoint value

    Notes
    -----
    Assumes directions on the complex plane
    """
    # Use complex numbers as coord grid
    ## To get final position
    directions = {"N": 1j, "E": 1, "S": -1j, "W": -1}
    rotations = {"L": 1j, "R": -1j}
    location = 0
    if start_waypoint is None:
        waypoint = False
        start_waypoint = 1
    else:
        waypoint = True

    for operation, amount in instructions:
        if operation in directions:
            if waypoint:
                start_waypoint += directions[operation] * amount
            else:
                location += directions[operation] * amount
        elif operation in rotations:
            start_waypoint *= rotations[operation] ** (amount / 90)
        else:
            location += start_waypoint * amount
    return location, start_waypoint


def get_manhattan_distance(location: complex) -> int:
    """Gets Manhattan distance from complex location

    Parameters
    ----------
    location : complex
        direction in complex co-coordinates

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
PART_2_LOCATION, PART_2_DIRECTION = run_path(DATA, start_waypoint=(10 + 1j))
PART_2_ANS = get_manhattan_distance(PART_2_LOCATION)
PART_2_TIME_MS = (timeit.default_timer() - PART_2_START_TIME) * 1000

if __name__ == "__main__":
    print(f"{PART_1_ANS=} Manhattan Distance from start position\n")
    print(f"{PART_2_ANS=} Manhattan Distance from start position\n")

    print(f"Timed Results:\n{PART_1_TIME_MS=:.3f}\n{PART_2_TIME_MS=:.3f}\n")
