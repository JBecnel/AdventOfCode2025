points = []
file_name = "sample_input9.txt"
file_name = "input9.txt"
with open(file_name, 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            num1, num2 = line.split(',')
            points.append((int(num1), int(num2)))


n = len(points)
max_area = 0
for i in range(n):
    for j in range(i + 1, n):
        p1 = points[i]
        p2 = points[j]
        area = abs(p1[0] - p2[0]+1) * abs(p1[1] - p2[1]+1)
        if area > max_area:
            max_area = area
print("Maximum area of rectangle formed by any two points:", max_area)