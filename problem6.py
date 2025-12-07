lines = [ ]
file_name = "sample_input6.txt"
file_name = "input6.txt"
with open(file_name, 'r') as file:
    lines = file.readlines()
    lines = [line.strip().split() for line in lines]
    print(len(lines))

print(lines)

total = 0
for i in range(len(lines[0])):
    num1 = int(lines[0][i])
    num2 = int(lines[1][i])
    num3 = int(lines[2][i])
    num4 = int(lines[3][i])
    operation = lines[4][i]
    
    if operation == '+':
        result = num1 + num2 + num3 + num4
    else:
        result = num1 * num2 * num3 * num4

    total += result

print("Total:", total)