""" Solution to Day 15 of Advent of Code 2020 """
import timeit
import typing as ty

# Constants
DATA = [1, 17, 0, 10, 18, 11, 6]


def get_last_elements(
    data: ty.List[int], target: int, number_of_elements: int = 2
) -> ty.List[int]:
    """Gets (most recent) last number_of_elements in a list which are equal to target

    Parameters
    ----------
    data : list
        of data to search through
    target : int
        number to target
    number_of_elements : int
        how many integers to obtain the indicesr

    Returns
    -------
    elements : list
        of idxes of data which are equal to target
    """
    elements = []
    # Search backwards through the data
    for idx, num in enumerate(data[::-1]):
        if len(elements) >= number_of_elements:
            break
        if num == target:
            elements.append(idx)
    return elements


def get_idx_in_sequence(
    starting_numbers: ty.List[int], target_seq_number: int
) -> ty.Tuple[ty.List[int], int]:
    """Returns the index value given a list of starting numbers

    Parameters
    ----------
    starting_numbers : list
        list of starting ints
    target_seq_number : int
        target number of sequence (starting from 1)

    Returns
    -------
    numbers_spoken, result : tuple
        numbers_spoken : list
            of ints/results spoken
        results : int
            final answer at target_index
    """
    spoken_numbers = []
    for game_idx in range(target_seq_number):
        if game_idx < len(starting_numbers):
            result = starting_numbers[game_idx]
        elif spoken_numbers[-1] not in spoken_numbers[:-2]:
            result = 0
        else:
            times_appeared = get_last_elements(spoken_numbers, spoken_numbers[-1])
            result = times_appeared[-1] - times_appeared[-2]
        spoken_numbers.append(result)
    return spoken_numbers, spoken_numbers[target_seq_number - 1]


# Answers
PART_1_START_TIME = timeit.default_timer()


TARGET_IDX_PART_1 = 2020

PART_1_ANS = get_idx_in_sequence(DATA, TARGET_IDX_PART_1)[1]
PART_1_TIME_MS = (timeit.default_timer() - PART_1_START_TIME) * 1000

PART_2_START_TIME = timeit.default_timer()

TARGET_IDX_PART_2 = 30_000_000


# PART_2_ANS = get_idx_in_sequence(DATA, TARGET_IDX_PART_2)[1]
PART_2_ANS = "TODO"
PART_2_TIME_MS = (timeit.default_timer() - PART_2_START_TIME) * 1000

if __name__ == "__main__":
    print(f"{PART_1_ANS=}\n")
    print(f"{PART_2_ANS=}\n")

    print(f"Timed Results:\n{PART_1_TIME_MS=:.3f}\n{PART_2_TIME_MS:.3f}\n")
