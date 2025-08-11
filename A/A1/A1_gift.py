import random
import matplotlib.pyplot as plt

# Function to generate random points
def generate_random_points(n):
    return [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n)]

# Function to determine if a triplet (p, q, r) is counterclockwise
def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    if val == 0:
        return 0
    elif val > 0:
        return 1
    else:
        return 2

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
            if orientation(points[p], points[i], points[q]) == 2:
                q = i
                
        p = q
        
        if p == l:
            break

    return hull

# Generate 100 random points
points = generate_random_points(100)

# Find the convex hull using the Gift Wrapping algorithm
convex_hull = gift_wrapping(points)

# Plot the points and the convex hull
plt.scatter(*zip(*points))
plt.plot(*zip(*convex_hull), 'r-')
plt.show()

# Function to test the convex hull algorithm
def test_gift_wrapping():
    # Test points (known convex hull is manually calculated)
    test_points = [(0, 0), (1, 1), (2, 2), (3, 1), (2, 0), (1, -1)]
    expected_hull = [(0, 0), (1, -1), (3, 1), (2, 2)]

    # Find the convex hull using the Gift Wrapping algorithm
    convex_hull = gift_wrapping(test_points)

    # Check if the result matches the expected convex hull
    assert set(convex_hull) == set(expected_hull), "Test failed: Convex hull does not match expected result"

    print("Test passed: Convex hull matches expected result")

    # Visualize the points and the convex hull
    plt.scatter(*zip(*test_points))
    plt.plot(*zip(*convex_hull), 'r-')
    plt.show()

# Run the test
test_gift_wrapping()
