import random
import matplotlib.pyplot as plt

# Function to generate random points
def generate_random_points(n):
    return [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n)]

# Function to determine if three points make a counter-clockwise turn
def ccw(p1, p2, p3):
    return (p2[1] - p1[1]) * (p3[0] - p2[0]) > (p2[0] - p1[0]) * (p3[1] - p2[1])

# Incremental algorithm to find the convex hull
def incremental_convex_hull(points):
    points = sorted(points)  # Sort points by x-coordinate
    hull = []

    # Lower hull
    for p in points:
        while len(hull) >= 2 and not ccw(hull[-2], hull[-1], p):
            hull.pop()
        hull.append(p)

    # Upper hull
    for p in reversed(points):
        while len(hull) >= 2 and not ccw(hull[-2], hull[-1], p):
            hull.pop()
        hull.append(p)

    return hull[:-1]  # Remove the duplicate point at the end

# Generate 100 random points
points = generate_random_points(100)

# Find the convex hull using the incremental algorithm
convex_hull = incremental_convex_hull(points)

# Plot the points and the convex hull
plt.scatter(*zip(*points))
plt.plot(*zip(*convex_hull), 'r-')
plt.show()
