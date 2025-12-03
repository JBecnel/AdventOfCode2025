def find_largest_between(nums, start, stop):
    
    
    max = nums[start]
    index = start
    for i in range(start, stop):
        if nums[i] > max:
            max = nums[i]
            index = i
    return index

def find_max(line):
    digits = 12*[0]
    nums = [int(line[i]) for i in range(len(line))]
    #print(nums)
    
    length = len(line)
    
    index = 0
    for i in range(0,12):
        index = find_largest_between(nums, index, length -12 + i+1)
        digits[i] = nums[index]
        index = index +1

    #print(digits)
    max_num = 0
    for d in digits:
        max_num = max_num * 10 + d
    
    return max_num

file_name = "sample_input3.txt"
file_name = "input3.txt"
with open(file_name, 'r') as file:
    total = 0
    for line in file:
        line = line.strip()
        max_num = find_max(line)
        #print(max_num)
        total += max_num
    print("Total:", total)