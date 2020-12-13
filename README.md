# Advent of Code
![Language (Python)](https://img.shields.io/badge/powered_by-Python-blue.svg?style=flat) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![Imports: isort](https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat&labelColor=ef8336)](https://pycqa.github.io/isort/)

Solutions to the [Advent of Code](https://adventofcode.com/) challenges.

Puzzle descriptions have not been shared in this repo. This is [per request](https://www.reddit.com/r/adventofcode/comments/k99rod/sharing_input_data_were_we_requested_not_to/) from [the AoC creator](https://github.com/topaz) and many others over countless threads [here](https://www.reddit.com/r/adventofcode/).

All problems can be found fully described [here](https://adventofcode.com/2020) as well as [previous years](https://adventofcode.com/2020/events).

These solutions are not designed to be the fastest computationally. They are simply the first ones I thought of.



## Dependencies

These solutions use [Poetry](https://poetry.eustace.io/) for packaging and dependencies:

```
poetry install --no-dev
```

- `numpy`
- `sympy`

These solutions require a version of `Python >= 3.8`

### Development dependencies

```
poetry install
```

- `pylint`
- `black`
- `isort`

## Poetry scripts

```bash
poetry run lint                                     # Runs: pylint
poetry run format                                   # Runs: isort & Black formatting on files
poetry run check_format                             # Checks: Black formatting
poetry run check_isort                              # Checks: isort formatter on files
poetry run python ./YYYY/day_XX/day_XX_solution.py  # Runs: solution for given year/day
poetry run all_solutions                            # Runs: all year(s) code solutions
```

## Structure
This repository has the following structure:
`root/year/day_{x}/`

Where each day contains an `input.txt` and a `day_xx_solution.py`.

When executed, each solution script prints the answer (and time taken) to each challenge part.

### Note

In order for `poetry run all_solutions` function to work properly the following variables must be preset:
* `PART_1_ANS`, `PART_2_ANS`
* `PART_1_TIME_MS`, `PART_2_TIME_MS`

If these are not, there will be no error (failsafe) rather the day solutions will just not print


## TODO
* improve singular day running `poetry run YYYY-DD` from function
* possibly run timing iteratively
* possibly graph timing for each day's solutions
