def is_point_in_polygon_on_edge_ok(point, polygon_vertices):
    """
    Ray Casting Algorithm modified to accept points on the boundary as "inside".
    Point is a tuple (x, y). Polygon is a list of tuples [(x1, y1), ...].
    """
    x, y = point
    n = len(polygon_vertices)
    inside = False

    for i in range(n):
        p1_x, p1_y = polygon_vertices[i]
        p2_x, p2_y = polygon_vertices[(i + 1) % n]

        # Check if the point lies exactly on an edge
        if min(p1_x, p2_x) <= x <= max(p1_x, p2_x) and \
           min(p1_y, p2_y) <= y <= max(p1_y, p2_y):
            # Check for collinearity to confirm it's on the line segment
            if (p2_x - p1_x) * (y - p1_y) == (p2_y - p1_y) * (x - p1_x):
                return True # Point is on the boundary

        # Original ray casting logic (for strictly inside points)
        if ((p1_y <= y < p2_y) or (p2_y <= y < p1_y)) and \
           (x < (p2_x - p1_x) * (y - p1_y) / (p2_y - p1_y) + p1_x):
            inside = not inside
            
    return inside

def segments_intersect_on_edge_ok(p1, p2, p3, p4):
    """
    Check if line segment (p1, p2) intersects with (p3, p4).
    Returns True only for strictly crossing intersections (not boundary overlaps).
    Points are tuples (x, y).
    """
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4

    denom = (y4 - y3) * (x2 - x1) - (x4 - x3) * (y2 - y1)
    if denom == 0:
        # Collinear or parallel. If collinear and overlapping, this is allowed, so return False for "strict intersection"
        # Since we allow boundary overlap, we only care about real "crossing" intersections.
        return False

    ua = ((x4 - x3) * (y1 - y3) - (y4 - y3) * (x1 - x3)) / denom
    ub = ((x2 - x1) * (y1 - y3) - (y2 - y1) * (x1 - x3)) / denom

    # The key change: allow ua/ub to be exactly 0 or 1 (endpoints touching/overlapping)
    # Return True *only* for strict intersections where both segments cross internal space
    if 0 < ua < 1 and 0 < ub < 1:
        return True
    return False

def is_rectangle_inside_polygon_on_edge_ok(rectangle_vertices, polygon_vertices):
    """
    Determines if an entire rectangle is inside or on the boundary of a non-convex polygon.
    """
    # 1. Check if all rectangle corners are inside or on the boundary
    for point in rectangle_vertices:
        if not is_point_in_polygon_on_edge_ok(point, polygon_vertices):
            return False

    # 2. Check for STRICT intersections between rectangle edges and polygon edges
    rect_edges = []
    for i in range(len(rectangle_vertices)):
        p1 = rectangle_vertices[i]
        p2 = rectangle_vertices[(i + 1) % len(rectangle_vertices)]
        rect_edges.append((p1, p2))

    poly_edges = []
    for i in range(len(polygon_vertices)):
        p1 = polygon_vertices[i]
        p2 = polygon_vertices[(i + 1) % len(polygon_vertices)]
        poly_edges.append((p1, p2))

    for rect_edge in rect_edges:
        for poly_edge in poly_edges:
            # We use the modified function that returns False for allowed boundary overlaps/collinearity
            if segments_intersect_on_edge_ok(rect_edge[0], rect_edge[1], poly_edge[0], poly_edge[1]):
                return False

    return True


non_convex_poly = [(0, 0), (10, 0), (10, 10), (5, 5), (0, 10)]

# A rectangle that sits perfectly on the bottom edge (0,0) to (10,0)
rect_on_edge = [(1, 0), (9, 0), (9, 1), (1, 1)] 

# A rectangle that touches the interior corner (5,5) with one edge
rect_touching_corner = [(4, 4), (6, 4), (6, 5), (4, 5)]

print(f"Rectangle rect_on_edge is inside/on boundary: {is_rectangle_inside_polygon_on_edge_ok(rect_on_edge, non_convex_poly)}")
print(f"Rectangle rect_touching_corner is inside/on boundary: {is_rectangle_inside_polygon_on_edge_ok(rect_touching_corner, non_convex_poly)}")

points = []
file_name = "sample_input9.txt"
file_name = "input9.txt"
with open(file_name, 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            num1, num2 = line.split(',')
            points.append((int(num1), int(num2)))


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

        
        #print(p,q, corners)
        if (is_rectangle_inside_polygon_on_edge_ok(corners, points)):            
                #print("inside   ")
                base = abs(p[0] - q[0]) + 1
                height = abs(p[1] - q[1]) + 1
                area = base * height
                if area > max_area:
                    max_area = area

print("Maximum area of rectangle formed by any two points:", max_area)