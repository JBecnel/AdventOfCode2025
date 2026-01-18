from math import prod

# Define constants for file name and end range
FILE_NAME = "input12.txt"
END_RANGE = 27


with open(FILE_NAME, 'r') as file:
    lines = file.read().split('\n')


present_sizes = [sum(line.count('#') for line in lines[i:i + 3]) for i in range(1, END_RANGE, 5)]


valid_present_count = 0


for line in lines[END_RANGE+3:]:
    delimiter_index = line.index(':')  # Find the delimiter position
    max_area = 1
    for dim in line[:delimiter_index].split('x'):
        max_area *= int(dim)
    
    presents = [int(quantity) for quantity in line[delimiter_index + 1:].split()]  # Extract present quantities
    
    
    sum = 0
    for i in range(len(presents)):
        sum += presents[i] * present_sizes[i]
    
    if max_area - sum >= 0:
        valid_present_count += 1  # Increment count if valid

# Output the total count of valid presents
print(valid_present_count)