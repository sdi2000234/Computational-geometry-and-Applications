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

# Generate 100 random points
points = generate_random_points(100)
points = sorted(points)  # Sort points by x-coordinate for divide and conquer

# Find the convex hull using the Divide and Conquer algorithm
convex_hull = divide_and_conquer(points)

# Close the hull by appending the first point at the end
convex_hull.append(convex_hull[0])

# Plot the points and the convex hull
plt.scatter(*zip(*points))
plt.plot(*zip(*convex_hull), 'r-')
plt.show()

# Function to test the convex hull algorithm
def test_divide_and_conquer():
    # Test points (known convex hull is manually calculated)
    test_points = [(0, 0), (1, 1), (2, 2), (3, 1), (2, 0), (1, -1)]
    expected_hull = [(0, 0), (1, -1), (3, 1), (2, 2)]

    # Find the convex hull using the Divide and Conquer algorithm
    convex_hull = divide_and_conquer(test_points)

    # Close the hull by appending the first point at the end
    convex_hull.append(convex_hull[0])

    # Check if the result matches the expected convex hull
    assert set(convex_hull) == set(expected_hull), "Test failed: Convex hull does not match expected result"

    print("Test passed: Convex hull matches expected result")

    # Visualize the points and the convex hull
    plt.scatter(*zip(*test_points))
    plt.plot(*zip(*convex_hull), 'r-')
    plt.show()

# Run the test
test_divide_and_conquer()
