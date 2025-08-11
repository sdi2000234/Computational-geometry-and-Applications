import random
import matplotlib.pyplot as plt

# Function to generate random points
def generate_random_points(n):
    return [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n)]

# Function to determine if three points make a counter-clockwise turn
def ccw(p1, p2, p3):
    return (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p2[0] - p1[0]) * (p3[1] - p2[1]) > 0

# Incremental algorithm to find the convex hull
def incremental_convex_hull(points):
    points = sorted(points)  # Sort points by x-coordinate
    lower_hull = []
    upper_hull = []

    # Lower hull
    for p in points:
        while len(lower_hull) >= 2 and not ccw(lower_hull[-2], lower_hull[-1], p):
            lower_hull.pop()
        lower_hull.append(p)

    # Upper hull
    for p in reversed(points):
        while len(upper_hull) >= 2 and not ccw(upper_hull[-2], upper_hull[-1], p):
            upper_hull.pop()
        upper_hull.append(p)

    return lower_hull[:-1] + upper_hull[:-1]  # Remove the duplicate points

# Function to merge two hulls
def merge_hulls(hull1, hull2):
    merged_hull = hull1 + hull2
    return incremental_convex_hull(merged_hull)

# Divide and Conquer algorithm to find the convex hull
def divide_and_conquer(points):
    if len(points) <= 3:
        return incremental_convex_hull(points)  # Use incremental algorithm for small sets

    mid = len(points) // 2
    left_hull = divide_and_conquer(points[:mid])
    right_hull = divide_and_conquer(points[mid:])

    return merge_hulls(left_hull, right_hull)

# Gift Wrapping algorithm to find the convex hull
def gift_wrapping(points):
    n = len(points)
    if n < 3:
        return points

    hull = []
    
    # Find the leftmost point
    l = min(range(n), key=lambda i: points[i][0])
    
    p = l
    while True:
        hull.append(points[p])
        q = (p + 1) % n
        
        for i in range(n):
            if ccw(points[p], points[i], points[q]):
                q = i
                
        p = q
        
        if p == l:
            break

    return hull

# Function to calculate the distance of a point from a line defined by two points
def distance(p, a, b):
    return abs((b[0] - a[0]) * (a[1] - p[1]) - (a[0] - p[0]) * (b[1] - a[1]))

# QuickHull algorithm to find the convex hull
def quickhull(points):
    if len(points) <= 3:
        return points

    # Find the points with the minimum and maximum x-coordinates
    min_x = min(points, key=lambda p: p[0])
    max_x = max(points, key=lambda p: p[0])

    def find_hull(pts, a, b):
        if not pts:
            return []
        p = max(pts, key=lambda p: distance(p, a, b))
        pts_left = [pt for pt in pts if ccw(a, p, pt)]
        pts_right = [pt for pt in pts if ccw(p, b, pt)]
        return find_hull(pts_left, a, p) + [p] + find_hull(pts_right, p, b)

    left_set = [p for p in points if ccw(min_x, max_x, p)]
    right_set = [p for p in points if ccw(max_x, min_x, p)]

    left_hull = find_hull(left_set, min_x, max_x)
    right_hull = find_hull(right_set, max_x, min_x)

    return [min_x] + left_hull + [max_x] + right_hull

# Generate 100 random points
points = generate_random_points(100)

# Find the convex hull using different algorithms
hull_incremental = incremental_convex_hull(points)
hull_gift_wrapping = gift_wrapping(points)
hull_divide_and_conquer = divide_and_conquer(points)
hull_quickhull = quickhull(points)

# Close the hulls by appending the first point at the end
hull_incremental.append(hull_incremental[0])
hull_gift_wrapping.append(hull_gift_wrapping[0])
hull_divide_and_conquer.append(hull_divide_and_conquer[0])
hull_quickhull.append(hull_quickhull[0])

# Plot the points and the convex hulls
plt.figure(figsize=(10, 10))

# Incremental algorithm
plt.subplot(2, 2, 1)
plt.title("Incremental Algorithm")
plt.scatter(*zip(*points))
plt.plot(*zip(*hull_incremental), 'r-')

# Gift Wrapping algorithm
plt.subplot(2, 2, 2)
plt.title("Gift Wrapping Algorithm")
plt.scatter(*zip(*points))
plt.plot(*zip(*hull_gift_wrapping), 'r-')

# Divide and Conquer algorithm
plt.subplot(2, 2, 3)
plt.title("Divide and Conquer Algorithm")
plt.scatter(*zip(*points))
plt.plot(*zip(*hull_divide_and_conquer), 'r-')

# QuickHull algorithm
plt.subplot(2, 2, 4)
plt.title("QuickHull Algorithm")
plt.scatter(*zip(*points))
plt.plot(*zip(*hull_quickhull), 'r-')

plt.tight_layout()
plt.show()
