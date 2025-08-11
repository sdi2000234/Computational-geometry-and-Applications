import random
import numpy as np
from scipy.spatial import ConvexHull
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

# Function to generate random points in 3D
def generate_random_points_3d(n):
    return np.random.rand(n, 3) * 100

# Function to calculate the convex hull using QuickHull algorithm in 3D
def quickhull_3d(points):
    hull = ConvexHull(points)
    return hull

# Function to animate the convex hull construction in 3D
def animate_convex_hull_3d(points, hull):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(points[:, 0], points[:, 1], points[:, 2], label='Points')

    def update(frame):
        ax.cla()
        ax.scatter(points[:, 0], points[:, 1], points[:, 2], label='Points')
        for simplex in hull.simplices[:frame + 1]:
            simplex = np.append(simplex, simplex[0])  # Cycle back to the first vertex
            ax.plot(points[simplex, 0], points[simplex, 1], points[simplex, 2], 'r-')
        ax.legend()

    ani = FuncAnimation(fig, update, frames=len(hull.simplices), repeat=False)
    plt.show()

# Generate random points in 3D
points_3d = generate_random_points_3d(100)

# Calculate the convex hull
hull_3d = quickhull_3d(points_3d)

# Animate the convex hull construction
animate_convex_hull_3d(points_3d, hull_3d)
