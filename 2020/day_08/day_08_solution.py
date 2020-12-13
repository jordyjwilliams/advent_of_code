""" Solution to Day 08 of Advent of Code 2020 """
import timeit
import typing as ty
from pathlib import Path

# Constants
DATA_PATH = Path.resolve(Path(__file__).parent)
OPERATIONS = ["acc", "jmp", "nop"]

with open(DATA_PATH / "input.txt") as input_file:
    DATA = input_file.readlines()


# Data parsing functions
def run_instruction(
    instruction: str, current_idx: int, arg: int, accumulator: int
) -> ty.Tuple[int, int]:
    """run instruction given by string

    Parameters
    ----------
    instruction : str
        instruction, line of input
    current_idx : int
        current index values
    arg : int
        argument from input
    accumulator : int
        accumulator value - to be updated

    Returns
    -------
    current_idx : int
        modified current index after instruction
    accumulator : int
        modified accumulator after instruction

    Raises
    ------
    ValueError if instruction not supported

    Notes
    -----
    * dependent on instruction not all values may be modified
    * current operations are hardcoded
    """
    if instruction not in OPERATIONS:
        raise ValueError(f"Instruction must be one of {OPERATIONS}")
    if instruction in ["acc", "nop"]:
        current_idx += 1
        if instruction == "acc":
            accumulator += arg
    elif instruction == "jmp":
        current_idx += arg
    return current_idx, accumulator


def run_loop(data: ty.List[str]) -> ty.Tuple[int, int, bool]:
    """Run loop for list of boot code strings

    Parameters
    ----------
    data : list
        list of input boot codes

    Returns
    -------
    accumulator : int
        accumulator value
    current_index : int
        current index on loop exit
    complete_boot_loop : bool
        if loop completed

    Notes
    -----
    Will run until:
        * complete (run idx same as length of data)
        * or the same instruction is ran twice (boot loop)
    """
    accumulator = 0
    current_idx = 0
    lines_ran = []
    while True:
        if current_idx in lines_ran:
            complete_boot_loop = False
            return accumulator, current_idx, complete_boot_loop
        if current_idx == len(data):
            complete_boot_loop = True
            return accumulator, current_idx, complete_boot_loop
        line = data[current_idx]
        func_key, arg = line.split(" ")
        arg = int(arg)
        lines_ran.append(current_idx)
        current_idx, accumulator = run_instruction(
            func_key, current_idx, arg, accumulator
        )


# Answers
PART_1_START_TIME = timeit.default_timer()

PART_1_ANS, BREAKS_AT_IDX, _ = run_loop(DATA)
PART_1_TIME_MS = (timeit.default_timer() - PART_1_START_TIME) * 1000

PART_2_START_TIME = timeit.default_timer()
LINE_IDXS_TO_SWITCH = [
    idx for idx, line in enumerate(DATA) if "nop" in line or "jmp" in line
]

for idx in LINE_IDXS_TO_SWITCH:
    NEW_DATA = list(DATA)
    NEW_DATA[idx] = (
        NEW_DATA[idx].replace("nop", "jmp")
        if "nop" in NEW_DATA[idx]
        else NEW_DATA[idx].replace("jmp", "nop")
    )
    ACC, _, COMPLETE = run_loop(NEW_DATA)
    if COMPLETE:
        MODIFY_INDEX = idx
        break

PART_2_ANS = ACC
PART_2_TIME_MS = (timeit.default_timer() - PART_2_START_TIME) * 1000

if __name__ == "__main__":
    print(f"{PART_1_ANS=} accumulator value. Idx: {BREAKS_AT_IDX} causes inf loop\n")
    print(f"{PART_2_ANS=} accumulator value. Changing idx: {MODIFY_INDEX} fixes\n")

    print(f"Timed Results:\n{PART_1_TIME_MS=:.3f}\n{PART_2_TIME_MS=:.3f}\n")
