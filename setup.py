#!/usr/bin/env python3

from cx_Freeze import setup, Executable
import sys

sys.setrecursionlimit(10000)

setup(
    name = "CSgui",
    version = "0.1",
    description = "Citizen scientis data validation - Graphical User Interface",
    executables = [Executable("main.py")]
)

build_options = {
    'excludes': ['importlib.resources']
}