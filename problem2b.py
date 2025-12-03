import re

def is_entirely_repeated(s):
    """
    Checks if a string is composed entirely of a single repeated pattern.

    Examples:
    "aaaaaa" -> True
    "ababab" -> True
    "abcabc" -> True
    "abcabcabc" -> True
    "hellohello" -> True
    "hello world" -> False (spaces break the exact pattern match)
    "abcab" -> False (doesn't repeat fully to the end)
    "a" -> False (requires at least one repetition due to the '+' quantifier)
    """
    # Regex pattern: ^(.+)\1+$
    pattern = re.compile(r"^(.+)\1+$")
    
    # re.match returns a match object if the pattern matches the start of the string,
    # otherwise it returns None. Since we use ^ and $, we cover the whole string.
    if pattern.match(s):
        return True
    else:
        return False


file_name = "sample_input2.txt"
file_name = "input2.txt"
with open(file_name, 'r') as file:
    content = file.read()
    
lines = content.split(',')
parsed_data = []

for line in lines:
    parts = line.strip().split('-')
    parsed_data.append(parts)

total = 0
for m, M in parsed_data:
    start = int(m)
    stop = int(M)
    count = 0
    for num in range(start, stop + 1):
        s = str(num)
        if is_entirely_repeated(s):
            total += num

print(total)