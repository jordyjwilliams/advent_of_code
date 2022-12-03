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
    # Part 1 maps
    opp_score_map = {"A": 1, "B": 2, "C": 3}
    player_score_map = {"X": 1, "Y": 2, "Z": 3}
    game_result_map = {"AY": 6, "AZ": 0, "BX": 0, "BZ": 6, "CX": 6, "CY": 0}
    # Part 2 maps
    result_score_map = {"X": 0, "Y": 3, "Z": 6}
    loss_score_map = {"A": 3, "B": 1, "C": 2}
    win_score_map = {"A": 2, "B": 3, "C": 1}

    scores = []
    for line in data:
        opp, result = line.replace("\n", "").split(" ")
        opp_score = opp_score_map[opp]
        player_score = (
            result_score_map[result] if result_in_data else player_score_map[result]
        )
        if not result_in_data:
            player_score += (
                3 if (player_score == opp_score) else game_result_map[opp + result]
            )
        else:
            switcher = {
                0: loss_score_map[opp],
                3: opp_score,
                6: win_score_map[opp]
            }
            player_score += switcher.get(player_score, 0)
        scores.append(player_score)
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
