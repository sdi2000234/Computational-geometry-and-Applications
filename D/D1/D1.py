import numpy as np
import matplotlib.pyplot as plt

class KDTreeNode:
    def __init__(self, point, left=None, right=None):
        self.point = point
        self.left = left
        self.right = right

def build_kd_tree(points, depth=0):
    if len(points) == 0:
        return None

    # Select axis based on depth so that axis cycles through all valid values
    k = len(points[0])
    axis = depth % k

    # Sort point list and choose median as pivot element
    points.sort(key=lambda x: x[axis])
    median = len(points) // 2

    # Create node and construct subtrees
    return KDTreeNode(
        point=points[median],
        left=build_kd_tree(points[:median], depth + 1),
        right=build_kd_tree(points[median + 1:], depth + 1)
    )

def visualize_kd_tree(node, depth=0, bounds=[(0, 100), (0, 100)], ax=None):
    if node is None:
        return

    k = len(node.point)
    axis = depth % k

    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))

    # Draw point
    ax.plot(node.point[0], node.point[1], 'ro')

    # Draw splitting line
    if axis == 0:
        ax.plot([node.point[0], node.point[0]], bounds[1], 'k-')
        visualize_kd_tree(node.left, depth + 1, [(bounds[0][0], node.point[0]), bounds[1]], ax)
        visualize_kd_tree(node.right, depth + 1, [(node.point[0], bounds[0][1]), bounds[1]], ax)
    else:
        ax.plot(bounds[0], [node.point[1], node.point[1]], 'k-')
        visualize_kd_tree(node.left, depth + 1, [bounds[0], (bounds[1][0], node.point[1])], ax)
        visualize_kd_tree(node.right, depth + 1, [bounds[0], (node.point[1], bounds[1][1])], ax)

    return ax

# Generate random points
points = np.random.rand(50, 2) * 100
points = points.tolist()

# Build KD-Tree
kd_tree = build_kd_tree(points)

# Visualize KD-Tree
ax = visualize_kd_tree(kd_tree)
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.title("KD-Tree Construction")
plt.show()
