"""Advent of Code 2025 - Day 1"""


from typing import Iterator
from pathlib import Path


def process_lines(path: str | Path):
	
	p = Path(path)
	count_zero = 0
	position = 50
	with p.open("r", encoding="utf-8") as fh:
		for raw in fh:
			line = raw.rstrip("\n\r")
			number = int(line[1:])
			
			count_zero = count_zero + (number // 100)
			num = number % 100

			old_position = position
			if line[0] == "L":
				position -= num
			else:
				position += num

			if position >= 100:
				count_zero = count_zero + 1

			if old_position != 0 and position <= 0:
				count_zero = count_zero + 1

			position = position % 100

			#print(line, num, position, count_zero,)		

	return count_zero
            


def main() -> None:
	#sample = Path("sample_input1.txt")
	sample = Path("input1.txt")
	count = process_lines(sample)
	print(count)
			


if __name__ == "__main__":
	main()

 