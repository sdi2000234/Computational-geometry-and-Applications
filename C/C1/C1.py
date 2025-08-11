import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay

# Function to generate random points in the plane
def generate_random_points(n):
    return np.random.rand(n, 2) * 100

# Function to perform Delaunay triangulation
def delaunay_triangulation(points):
    return Delaunay(points)

# Function to visualize the Delaunay triangulation
def visualize_delaunay(points, tri):
    plt.figure(figsize=(8, 8))
    plt.triplot(points[:, 0], points[:, 1], tri.simplices, 'r-', label='Delaunay Triangulation')
    plt.scatter(points[:, 0], points[:, 1], label='Points')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Delaunay Triangulation')
    plt.legend()
    plt.show()

# Generate random points in the plane
points = generate_random_points(50)

# Perform Delaunay triangulation
tri = delaunay_triangulation(points)

# Visualize the Delaunay triangulation
visualize_delaunay(points, tri)
