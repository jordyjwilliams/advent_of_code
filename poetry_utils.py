"""Utility & CLI functions"""  # pylint:disable-msg=C0415
import os
from glob import glob
import importlib.util
import sys
from pathlib import Path
import subprocess
from pylint import lint

MINIMUM_LINTER_SCORE = 10


def exit_on_result(success):
    """Shutdown with correct exit code"""
    return sys.exit(0) if success else sys.exit(1)


def run_black(check_only=True):
    """run black"""
    args = ["black", "."]
    if check_only:
        args.append("--check")
    return subprocess.run(args, check=False)


def run_lint():
    """Invoke pylint programmatically"""
    run = lint.Run(["./2020/"], do_exit=False)
    exit_on_result(run.linter.stats["global_note"] >= MINIMUM_LINTER_SCORE)


def check_format():
    """Invoke Black to check formatting"""
    exit_on_result(run_black(check_only=True).returncode == 0)


def run_format():
    """Invoke Black to apply formatting"""
    exit_on_result(run_black(check_only=False).returncode == 0)


def run_all_days():
    """ Runner to run all day solutions """
    # year, day dir structure
    solution_files = glob("./*/*/*solution*.py")
    for solution in solution_files:
        print(f"{solution}\n")
        # Hacky importing the solution module as will print answer
        mod_spec = importlib.util.spec_from_file_location("sol", solution)
        module = mod_spec.loader.exec_module(importlib.util.module_from_spec(mod_spec))
