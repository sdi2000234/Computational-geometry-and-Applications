import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay
import time

# Function to generate random points in the plane
def generate_random_points(n):
    return np.random.rand(n, 2) * 100

# Function to perform Delaunay triangulation
def delaunay_triangulation(points):
    return Delaunay(points)

# Function to visualize the Delaunay triangulation
def visualize_delaunay(points, tri, num_points):
    plt.figure(figsize=(8, 8))
    plt.triplot(points[:, 0], points[:, 1], tri.simplices, 'r-', label='Delaunay Triangulation')
    plt.scatter(points[:, 0], points[:, 1], label='Points')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(f'Delaunay Triangulation with {num_points} Points')
    plt.legend()
    plt.show()

# Function to analyze the behavior of Delaunay triangulation with increasing number of points
def analyze_delaunay_increasing_points(point_counts):
    times = []
    
    for num_points in point_counts:
        points = generate_random_points(num_points)
        start_time = time.time()
        tri = delaunay_triangulation(points)
        end_time = time.time()
        times.append(end_time - start_time)
        visualize_delaunay(points, tri, num_points)
    
    return times

# Define different sizes of point sets to analyze
point_counts = [10, 50, 100, 500, 1000, 5000]

# Analyze Delaunay triangulation with increasing number of points
times = analyze_delaunay_increasing_points(point_counts)

# Plot the time taken for each point set size
plt.figure(figsize=(8, 6))
plt.plot(point_counts, times, 'o-', label='Time Taken')
plt.xlabel('Number of Points')
plt.ylabel('Time (seconds)')
plt.title('Delaunay Triangulation Time Analysis')
plt.legend()
plt.show()
