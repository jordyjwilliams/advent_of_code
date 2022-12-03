""" Solution to Day 02 of Advent of Code 2022 """
import timeit
import typing as ty
from pathlib import Path

# Constants
DATA_PATH = Path.resolve(Path(__file__).parent)

# read data line by line
with open(DATA_PATH / "input.txt", encoding="UTF-8") as input_file:
    DATA = input_file.readlines()


def parse_dataline_to_scores(data: str, result_in_data: bool = False) -> ty.List[int]:
    """Total score for data line, returns list of integers.
    Selection result: 1: rock, 2: paper, 3: scissors
    Round result: 0: loss, 3: draw, 6: win

    Parameters
    ----------
    data : str
        input data format:
            Col1: Opponent: A - rock, B - paper, C - scissors
            result_in_data: False:
                Col2: Player: X - rock, Y - paper, Z - scissors
            result_in_data: True:
                Col2: Result: X - loss, Y - draw, Z - win
    result_in_data : bool, optional: default: False
        boolean for format of 2nd column. If True will be result.
        (Part 2).

    Returns
    -------
    scores : list[int]
        list of scores for each line
    """
    # Part 1 game map data
    result_map_player_data = {
        "AX": 4,  # opp: R, player: R, game: draw - [1 + 3]
        "AY": 8,  # opp: R, player: P, game: win - [2 + 6]
        "AZ": 3,  # opp: R, player: S, game: loss - [3 + 0]
        "BX": 1,  # opp: P, player: R, game: loss - [1 + 0]
        "BY": 5,  # opp: P, player: P, game: draw - [2 + 3]
        "BZ": 9,  # opp: P, player: S, game: win - [3 + 6]
        "CX": 7,  # opp: S, player: R, game: win - [1 + 6]
        "CY": 2,  # opp: S, player: P, game: loss - [2 + 0]
        "CZ": 6,  # opp: S, player: S, game: draw - [3 + 3]
    }
    # Part 2 game map data
    result_map_result_data = {
        "AX": 3,  # opp: R, game: loss, player: S - [3 + 0]
        "AY": 4,  # opp: R, game: draw, player: R - [1 + 3]
        "AZ": 8,  # opp: R, game: win, player: P - [2 + 6]
        "BX": 1,  # opp: P, game: loss, player: R - [1 + 0]
        "BY": 5,  # opp: P, game: draw, player: P - [2 + 3]
        "BZ": 9,  # opp: P, game: win, player: S - [3 + 6]
        "CX": 2,  # opp: S, game: loss, player: P - [2 + 0]
        "CY": 6,  # opp: S, game: draw, player: S - [3 + 3]
        "CZ": 7,  # opp: S, game: win, player: R - [1 + 6]
    }

    scores = []
    for line in data:
        game_data = line.replace("\n", "").replace(" ", "")
        scores.append(
            (
                result_map_result_data[game_data]
                if result_in_data
                else result_map_player_data[game_data]
            )
        )
    return scores


# Answers
PART_1_START_TIME = timeit.default_timer()
PART_1_ANS = sum(parse_dataline_to_scores(DATA, result_in_data=False))
PART_1_TIME_MS = (timeit.default_timer() - PART_1_START_TIME) * 1000

PART_2_START_TIME = timeit.default_timer()
PART_2_ANS = sum(parse_dataline_to_scores(DATA, result_in_data=True))
PART_2_TIME_MS = (timeit.default_timer() - PART_2_START_TIME) * 1000

if __name__ == "__main__":
    print(f"Part 1\nTotal 🪨 📜 ✂️ score: {PART_1_ANS}\n")
    print(f"Part 2\nTotal 🪨 📜 ✂️ score: {PART_2_ANS}\n")
    print(f"Timed Results:\n{PART_1_TIME_MS=:.3f}\n{PART_2_TIME_MS=:.3f}\n")
