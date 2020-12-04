# Advent of Code
![Language (Python)](https://img.shields.io/badge/powered_by-Python-blue.svg?style=flat) [![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Solutions to the [Advent of Code](https://adventofcode.com/) challenges.

These solutions are not designed to be the fastest computationally. They are simply the first ones I thought of.


## Dependencies

These solutions use [Poetry](https://poetry.eustace.io/) for packaging and dependencies:

```
poetry install --no-dev
```

- `numpy`

These solutions require a version of `Python >= 3.7`

### Development dependencies

```
poetry install
```

- `pylint`
- `black`

## Poetry scripts

```
poetry run lint                                     # run pylint
poetry run format                                   # run black formatter on files
poetry run check_format                             # check formatting
poetry run python ./YYYY/day_XX/day_XX_solution.py  # run solution for given year/day
poetry run all_solutions                            # run all year(s) code solutions
```

## Structure
This repository has the following structure:
`root/year/day_{x}/`

Where each day contains an `input.txt` and a `day_xx.py` solution.

Each solution script prints the answer to the challenge parts.


## TODO
* improve singular day running `poetry run YYYY-DD` from function
