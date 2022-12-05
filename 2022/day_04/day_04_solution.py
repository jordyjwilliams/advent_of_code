""" Solution to Day 04 of Advent of Code 2022 """
import timeit
from pathlib import Path

# Constants
DATA_PATH = Path.resolve(Path(__file__).parent)

# read data line by line
with open(DATA_PATH / "input.txt", encoding="UTF-8") as input_file:
    DATA = input_file.readlines()


def parse_dataline_to_containment(data: str, part2: bool = False) -> int:
    """Elf pair datalines. Returns number of contained/overlapping datasets.

    Parameters
    ----------
    data : str
        elf pair data AA-BB,XX-YY format
        data will be strings of ints
    part2 : bool, optional
        if True part 2 solution

    Returns
    -------
    contained : int
        number contained as specified in question
    """
    contained = 0
    for line in data:
        range_data = [[int(num) for num in itm.split("-")] for itm in line.split(",")]
        # part one, one range fully contains another
        ## TODO: cleanup this logic
        if (
            range_data[0][0] >= range_data[1][0]
            and range_data[0][1] <= range_data[1][1]
            or range_data[1][0] >= range_data[0][0]
            and range_data[1][1] <= range_data[0][1]
            and not part2
        ):
            contained += 1
        # part two, assignment pair ranges overlap (at all)
        ## TODO: invoke sets in nicer way.
        elif (
            set(range(range_data[0][0], range_data[0][1] + 1)).intersection(
                set(range(range_data[1][0], range_data[1][1] + 1))
            )
            and part2
        ):
            contained += 1
    return contained


# Answers
PART_1_START_TIME = timeit.default_timer()
PART_1_ANS = parse_dataline_to_containment(DATA, part2=False)
PART_1_TIME_MS = (timeit.default_timer() - PART_1_START_TIME) * 1000

PART_2_START_TIME = timeit.default_timer()
PART_2_ANS = parse_dataline_to_containment(DATA, part2=True)
PART_2_TIME_MS = (timeit.default_timer() - PART_2_START_TIME) * 1000

if __name__ == "__main__":
    print(f"Number assignment pairs fully contained: {PART_1_ANS} pairs\n")
    print(f"Number assignment pairs with overlapping ranges: {PART_2_ANS} pairs\n")

    print(f"Timed Results:\n{PART_1_TIME_MS=:.3f}\n{PART_2_TIME_MS=:.3f}\n")
