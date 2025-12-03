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
        length = len(s)
        half = length // 2
        if length % 2 == 0:
            left = s[:half]
            right = s[half:]
            if left == right:
                count += 1
                total += num

    #print(f"{m}-{M}: {num}  => {count}")

print(total)
