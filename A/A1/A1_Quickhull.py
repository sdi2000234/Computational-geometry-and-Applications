import random
import matplotlib.pyplot as plt

# Function to generate random points
def generate_random_points(n):
    return [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n)]

# Function to determine if three points make a counter-clockwise turn
def ccw(p1, p2, p3):
    return (p2[1] - p1[1]) * (p3[0] - p2[0]) > (p2[0] - p1[0]) * (p3[1] - p2[1])

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

# Find the convex hull using the QuickHull algorithm
convex_hull = quickhull(points)

# Plot the points and the convex hull
plt.scatter(*zip(*points))
plt.plot(*zip(*convex_hull + [convex_hull[0]]), 'r-')
plt.show()

# Function to test the convex hull algorithm
def test_quickhull():
    # Test points (known convex hull is manually calculated)
    test_points = [(0, 0), (1, 1), (2, 2), (3, 1), (2, 0), (1, -1)]
    expected_hull = [(0, 0), (1, -1), (3, 1), (2, 2)]

    # Find the convex hull using the QuickHull algorithm
    convex_hull = quickhull(test_points)

    # Check if the result matches the expected convex hull
    assert set(convex_hull) == set(expected_hull), "Test failed: Convex hull does not match expected result"

    print("Test passed: Convex hull matches expected result")

    # Visualize the points and the convex hull
    plt.scatter(*zip(*test_points))
    plt.plot(*zip(*convex_hull + [convex_hull[0]]), 'r-')
    plt.show()

# Run the test
test_quickhull()
