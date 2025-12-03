def count_less_than(s: str) -> int:
    n = (len(s)-1) // 2
    total = 0    
    for i in range(0, n, 1):
        total = total*10+9
    
    if len(s) % 2 == 1:
        return total 
    
    first_digit = int(s[0])
    middle_digit = int(s[len(s)//2])
    if first_digit == 1:
        return total
    else:
        total = total + (first_digit -1) * (total +1)    
    
    mid = len(s)//2
    if middle_digit < first_digit or mid == 1:
        return total
    elif middle_digit > first_digit:
        left = int(s[1:mid])
        return total + left +1 # +1 for 000
    elif middle_digit == first_digit:
        left = int(s[1:mid])
        right = int(s[(mid+1):].lstrip('0') or '0')
        return total + min(left, right)+1
    
with open('sample_input2.txt', 'r') as file:
    content = file.read()
    
lines = content.split(',')
parsed_data = []

for line in lines:
    parts = line.strip().split('-')
    parsed_data.append(parts)

for m, M in parsed_data:
    num = count_less_than(m)
    num2 = count_less_than(M)
    print(f"{m}-{M}: {num} {num2} => {num2 - num}")


