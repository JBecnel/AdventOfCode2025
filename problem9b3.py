points = []
file_name = "sample_input9.txt"
file_name = "input9.txt"
with open(file_name, 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            num1, num2 = line.split(',')
            points.append((int(num1), int(num2)))

import matplotlib.pyplot as plt

# Extract x and y coordinates
x_coords = [p[0] for p in points]
y_coords = [p[1] for p in points]

# Close the polygon by adding the first point at the end
x_coords.append(x_coords[0])
y_coords.append(y_coords[0])

# Plot the polygon
plt.figure(figsize=(10, 10))
plt.plot(x_coords, y_coords, 'b-', linewidth=2)
#plt.scatter(x_coords[:-1], y_coords[:-1], color='red', s=50)
plt.grid(True)
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Polygon')
plt.axis('equal')
plt.show()