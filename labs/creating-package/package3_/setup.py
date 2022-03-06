from setuptools import setup

from pathlib import Path

this_directory = Path(__file__).parent
long_description = (this_directory / "Readme.rst").read_text()

setup(
    long_description=long_description,
)
