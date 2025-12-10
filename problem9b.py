points = []
file_name = "sample_input9.txt"
file_name = "input9.txt"
with open(file_name, 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            num1, num2 = line.split(',')
            points.append((int(num1), int(num2)))
# two copies of the points sorted by x and y
points_sorted_by_x = sorted(points, key=lambda p: p[0])
points_sorted_by_y = sorted(points, key=lambda p: p[1])


points_sorted_by_x = sorted(points, key=lambda p: (p[0], p[1]) )
filtered_x = []
for i, p in enumerate(points_sorted_by_x):
    if i == 0 or points_sorted_by_x[i][0] != points_sorted_by_x[i-1][0]:
        filtered_x.append(p)
    elif i == len(points_sorted_by_x) - 1 or points_sorted_by_x[i+1][0] != points_sorted_by_x[i][0]:
        filtered_x.append(p)


points_sorted_by_y = sorted(points, key=lambda p: (p[1], p[0]))
filtered_y = []
for i, p in enumerate(points_sorted_by_y):
    if i == 0 or points_sorted_by_y[i][1] != points_sorted_by_y[i-1][1]:
        filtered_y.append(p)
    elif i == len(points_sorted_by_y) - 1 or points_sorted_by_y[i+1][1] != points_sorted_by_y[i][1]:
        filtered_y.append(p)

# keep only two points on each vertical or horizontal line (same x or same y)
# keep the points that are furthest apart
#print(points_sorted_by_x)
#print(points_sorted_by_y)
#print(filtered_x)
#print(filtered_y)

rect = [ ]
for i in range(len(filtered_x)-1):
    if filtered_x[i][0] == filtered_x[i+1][0]:
        for j in range(len(filtered_x)-1, i+1, -1):            
            if filtered_x[j][0] == filtered_x[j-1][0]:
                #base = filtered_x[j][0] - filtered_x[i][0] + 1
                # if left < right
                if abs(filtered_x[i][1] - filtered_x[i+1][1]) <= abs(filtered_x[j][1] - filtered_x[j-1][1]):                
                    # top left and bottom right
                    rect.append((filtered_x[i], (filtered_x[j][0], filtered_x[i+1][1])))
                else:
                    rect.append(((filtered_x[i][0], filtered_x[j-1][1]), filtered_x[i+1]))

                # Check if the last rectangle added is inside any previous rectangle
                last_rect = rect[-1]
                (x1_last, y1_last) = last_rect[0]
                (x2_last, y2_last) = last_rect[1]

                for k in range(len(rect) - 2, -1, -1):
                    (x1_prev, y1_prev) = rect[k][0]
                    (x2_prev, y2_prev) = rect[k][1]
                    
                    if (x1_prev <= x1_last and x2_last <= x2_prev and
                        y1_prev <= y1_last and y2_last <= y2_prev):
                        rect.pop()
                        break
print(len(rect))               
# traverse all pairs of points and calculate area if both points fit in any rectangle
# if so, calculate area and update max_area             
max_area = 0
for i in range(len(points)-1):
    for j in range(i+1, len(points)):
        p = points[i]
        q = points[j]
        for r in rect:
            (x1, y1) = r[0]
            (x2, y2) = r[1]
            if x1 <= p[0] <= x2 and y1 <= p[1] <= y2 and x1 <= q[0] <= x2 and y1 <= q[1] <= y2:
                base = abs(p[0] - q[0]) + 1
                height = abs(p[1] - q[1]) + 1
                area = base * height
                if area > max_area:
                    max_area = area
print(rect)
print("Maximum area of rectangle formed by any two points:", max_area)
# now for rectangles going in the y direction
rect = [ ]
for i in range(len(filtered_y)-1):
    if filtered_y[i][1] == filtered_y[i+1][1]:
        for j in range(len(filtered_y)-1, i+1, -1):            
            if filtered_y[j][1] == filtered_y[j-1][1]:
                #base = filtered_x[j][0] - filtered_x[i][0] + 1
                # if top < bottom
                if abs(filtered_y[i][0] - filtered_y[i+1][0]) <= abs(filtered_y[j][0] - filtered_y[j-1][0]):                
                    # top left and bottom right
                    rect.append((filtered_y[i], (filtered_y[i+1][0], filtered_y[j][1])))
                else:
                    rect.append(((filtered_y[j][0], filtered_y[i][1]), filtered_y[j]))
                # Check if the last rectangle added is inside any previous rectangle
                last_rect = rect[-1]
                (x1_last, y1_last) = last_rect[0]
                (x2_last, y2_last) = last_rect[1]

                for k in range(len(rect) - 2, -1, -1):
                    (x1_prev, y1_prev) = rect[k][0]
                    (x2_prev, y2_prev) = rect[k][1]
                    
                    if (x1_prev <= x1_last and x2_last <= x2_prev and
                        y1_prev <= y1_last and y2_last <= y2_prev):
                        rect.pop()
                        break
    
print(len(rect))
print(filtered_y)
print(rect)

max_area = 0
for i in range(len(points)-1):
    for j in range(i+1, len(points)):
        p = points[i]
        q = points[j]
        for r in rect:
            (x1, y1) = r[0]
            (x2, y2) = r[1]
            if x1 <= p[0] <= x2 and y1 <= p[1] <= y2 and x1 <= q[0] <= x2 and y1 <= q[1] <= y2:
                base = abs(p[0] - q[0]) + 1
                height = abs(p[1] - q[1]) + 1
                area = base * height
                if area > max_area:
                    max_area = area

print("Maximum area of rectangle formed by any two points:", max_area)