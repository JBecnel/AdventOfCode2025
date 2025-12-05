first_num = []
second_num = []
ingredients = []
file_name = "sample_input5.txt"
file_name = "input5.txt"
with open(file_name, 'r') as file:
    for line in file:
        line = line.strip()
        
        if line == '':
            # Blank line reached, start reading ingredients
            for remaining_line in file:
                remaining_line = remaining_line.strip()
                if remaining_line:
                    ingredients.append(int(remaining_line))
            break
        else:
            # Parse the #-# format
            parts = line.split('-')
            first_num.append(int(parts[0]))
            second_num.append(int(parts[1]))

print("First Numbers:", first_num)
print("Second Numbers:", second_num)
print("Ingredients:", ingredients)

count = 0
for ing in ingredients:
    for i in range(len(first_num)):
        if first_num[i] <= ing <= second_num[i]:
            count += 1
            break
print("Count of ingredients within ranges:", count)