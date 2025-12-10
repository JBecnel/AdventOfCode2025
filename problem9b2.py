points = []
file_name = "sample_input9.txt"
file_name = "input9.txt"
with open(file_name, 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            num1, num2 = line.split(',')
            points.append((int(num1), int(num2)))

max_x = max(p[0] for p in points)
max_y = max(p[1] for p in points)
min_x = min(p[0] for p in points)
min_y = min(p[1] for p in points)

print(max_x, min_x, max_y, min_y)

def is_point_in_polygon(point_x, point_y, polygon):
    """
    Determines if a point (point_x, point_y) is inside a non-convex polygon.

    The polygon is a list of (x, y) integer tuples.
    The algorithm uses the ray casting method (even-odd rule).
    """
    n = len(polygon)
    if n < 3:
        return False  # A polygon must have at least 3 vertices

    inside = False
    p1x, p1y = polygon[0]
    
    # Loop through each edge of the polygon
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]  # Wrap around to the first vertex for the last edge
        if (point_x == p2x and point_y == p2y) or (point_x == p1x and point_y == p1y):
            return True  # Point is a vertex of the polygon
        # Check if the ray from the point crosses the edge vertically
        if point_y > min(p1y, p2y) and point_y <= max(p1y, p2y):
            if point_x <= max(p1x, p2x):
                # Calculate the x-coordinate of the intersection point
                if p1y != p2y:
                    # Using integer arithmetic where possible to avoid precision issues
                    # with floats, though division for xints is necessary.
                    xinters = (point_y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                else:
                    xinters = p1x # Horizontal edge, xinters is p1x (or p2x)

                # If the ray crosses the edge to the left of the point, toggle the inside flag
                if p1x == p2x or point_x <= xinters:
                    inside = not inside

        p1x, p1y = p2x, p2y  # Move to the next point

    return inside

# Example Usage:
# A non-convex (concave) polygon shape (vertices are integers)
non_convex_poly = [(0, 0), (10, 0), (10, 10), (5, 5), (0, 10)]
point_inside = (5, 4)
point_outside = (5, 8)
point_on_edge = (0, 0) # This implementation treats points on edges as inside

print(f"Point {point_inside} inside? {is_point_in_polygon(point_inside[0], point_inside[1], non_convex_poly)}")
print(f"Point {point_outside} inside? {is_point_in_polygon(point_outside[0], point_outside[1], non_convex_poly)}")
print(f"Point {point_on_edge} inside? {is_point_in_polygon(point_on_edge[0], point_on_edge[1], non_convex_poly)}")





max_area = 0
for i in range(len(points)-1):
    for j in range(i+1, len(points)):
        p = points[i]
        q = points[j]
        corners = []
        corners.append((min(p[0], q[0]), min(p[1], q[1])))
        corners.append((max(p[0], q[0]), max(p[1], q[1])))
        corners.append((min(p[0], q[0]), max(p[1], q[1])))
        corners.append((max(p[0], q[0]), min(p[1], q[1])))

        corners.remove(p)
        corners.remove(q)
        #print(p,q, corners)
        if (is_point_in_polygon(corners[0][0], corners[0][1], points) and
            is_point_in_polygon(corners[1][0], corners[1][1], points)):
                #print("inside   ")
                base = abs(p[0] - q[0]) + 1
                height = abs(p[1] - q[1]) + 1
                area = base * height
                if area > max_area:
                    max_area = area

print("Maximum area of rectangle formed by any two points:", max_area)