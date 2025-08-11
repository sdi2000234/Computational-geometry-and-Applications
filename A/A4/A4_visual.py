import random
import matplotlib.pyplot as plt

# Function to generate random points
def generate_random_points(n):
    return [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n)]

# Function to determine if three points make a counter-clockwise turn
def ccw(p1, p2, p3):
    return (p2[1] - p1[1]) * (p3[0] - p2[0]) - (p2[0] - p1[0]) * (p3[1] - p2[1]) > 0

# Gift Wrapping algorithm to find the convex hull with visualization
def gift_wrapping_visualize(points):
    n = len(points)
    if n < 3:
        return points

    hull = []
    l = min(range(n), key=lambda i: points[i][0])  # Find the leftmost point
    p = l

    plt.figure(figsize=(10, 10))

    while True:
        hull.append(points[p])
        q = (p + 1) % n
        for i in range(n):
            if ccw(points[p], points[i], points[q]):
                q = i

        p = q
        if p == l:
            break

        # Plotting the current hull
        plt.clf()
        plt.scatter(*zip(*points), label='Points')
        hull_with_start = hull + [points[l]]
        plt.plot(*zip(*hull_with_start), 'r-', label='Current Hull')
        plt.scatter(*zip(*hull_with_start), color='red')
        plt.legend()
        plt.pause(0.5)  # Pause to visualize the steps

    hull.append(points[l])  # Close the hull

    # Final plot
    plt.clf()
    plt.scatter(*zip(*points), label='Points')
    plt.plot(*zip(*hull), 'r-', label='Final Hull')
    plt.scatter(*zip(*hull), color='red')
    plt.legend()
    plt.show()

    return hull

# Generate points including collinear points
points = generate_random_points(20)

# Find the convex hull using the Gift Wrapping algorithm with visualization
gift_wrapping_visualize(points)
