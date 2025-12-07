def process_numbers(num1, num2, num3, num4):
    

    nums = []    
    for i in range(len(num1)):
        num = 0
        flag = False
        if num1[i] != ' ' and num1[i] != '\n':
            num = num*10  + int(num1[i])
            flag = True
        if num2[i] != ' ' and num2[i] != '\n':
            num = num*10  + int(num2[i])
            flag = True
        if num3[i] != ' ' and num3[i] != '\n':
            num = num*10  + int(num3[i])
            flag = True
        if num4[i] != ' ' and num4[i] != '\n':
            num = num*10  + int(num4[i])
            flag = True
        if flag:
            nums.append(num)
    return nums

lines = [ ]
file_name = "sample_input6.txt"
file_name = "input6.txt"
with open(file_name, 'r') as file:
    lines = file.readlines()
    lines = [list(line) for line in lines]
    lines[4].append("")  # Ensure all lines have the same length
    print(len(lines))

index_of_operations = []
index_of_operations = [i for i, op in enumerate(lines[4]) if op == '*' or op == '+']

print("Indices of operations:", index_of_operations)
#print(lines)
#for line in lines:
#    print(len(line))
index_of_operations.append(len(lines[0]))  # Add end index
total = 0
for i in range(len(index_of_operations) - 1):
    start_index = index_of_operations[i]
    end_index = index_of_operations[i + 1]

    num1 = lines[0][start_index:end_index]
    num2 = lines[1][start_index:end_index]
    num3 = lines[2][start_index:end_index]
    num4 = lines[3][start_index:end_index]
    operation = lines[4][start_index]
    print(num1, num2, num3, num4, operation)
    nums = process_numbers(num1, num2, num3, num4)
    print(nums)
    if operation == '+':
        result = sum(nums)
    else:
        result = 1
        for num in nums:
            result *= num

    total += result

print("Total:", total)