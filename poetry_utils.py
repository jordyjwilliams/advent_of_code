"""Utility & CLI functions"""  # pylint:disable-msg=C0415
import importlib.util
import subprocess
import sys
from glob import glob

import pytest  # pylint:disable=E0401


def exit_on_result(success: bool):
    """Shutdown with correct exit code"""
    return sys.exit(0) if success else sys.exit(1)


def run_lint():
    """run linting using pytest-pylint"""
    args = ["-m", "pylint", "./2020/"]
    exit_on_result(pytest.main(args) == pytest.ExitCode.OK)


def run_black(check_only: bool = True):
    """run black"""
    args = ["black", "./"]
    if check_only:
        args.append("--check")
    return subprocess.run(args, check=False)


def run_isort(check_only: bool = True):
    """run isort"""
    args = ["isort", "."]
    if check_only:
        args.append("--diff")
    return subprocess.run(args, check=False)


def check_format():
    """Invoke Black to check formatting"""
    exit_on_result(run_black(check_only=True).returncode == 0)


def check_isort():
    """Invoke Black to check formatting"""
    exit_on_result(run_isort(check_only=True).returncode == 0)


def run_format():
    """Invoke isort and Black to apply formatting"""
    print("Running isort\n")
    run_isort(check_only=False)
    print("Running Black\n")
    exit_on_result(run_black(check_only=False).returncode == 0)


def run_all_days():
    """Runner to run all day solutions"""
    # year, day dir structure
    print("Note: Run each solution separatelyor more detailed print statements")
    solution_files = glob("./*/*/*solution*.py")
    for solution in sorted(solution_files):
        if "day_xx" in solution:
            break
        print(f"{solution}\n")
        mod_spec = importlib.util.spec_from_file_location("sol", solution)
        module = importlib.util.module_from_spec(mod_spec)
        mod_spec.loader.exec_module(module)
        try:
            print(f"Part 1:\n{module.PART_1_ANS}\n")
            print(f"Part 2:\n{module.PART_2_ANS}\n")
            print(
                f"Timed Results:\nPart 1: {module.PART_1_TIME_MS:.3f} ms\nPart 2: {module.PART_2_TIME_MS:.3f} ms\n"
            )
        except AttributeError:
            print("One of the required variable names is not preset")
