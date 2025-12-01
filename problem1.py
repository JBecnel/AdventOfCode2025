"""Advent of Code 2025 - Day 1 helpers

This module contains a simple function to read a text file line-by-line
and a tiny CLI demonstration that prints each line with its line number.
"""

from typing import Iterator
from pathlib import Path


def process_lines(path: str | Path):
	"""Yield lines from `path` one at a time, stripped of trailing newlines.

	- Skips empty lines (after stripping).
	- Opens file with UTF-8 encoding.

	Example:
		>>> for line in read_lines('sample_input1.txt'):
		...     print(line)
	"""
	p = Path(path)
	count_zero = 0
	position = 50
	with p.open("r", encoding="utf-8") as fh:
		for raw in fh:
			line = raw.rstrip("\n\r")
			number = int(line[1:])
			if line[0] == "L":
				position -= number
			else:
				position += number

			position = position % 100

			if position == 0:
				count_zero += 1

	return count_zero
            


def main() -> None:
	"""Simple CLI: read `sample_input1.txt` from the repo root and print lines.

	This is just a demonstration used while solving the puzzle.
	"""
	#sample = Path("sample_input1.txt")
	sample = Path("input1.txt")
	count = process_lines(sample)
	print(count)
			


if __name__ == "__main__":
	main()

 