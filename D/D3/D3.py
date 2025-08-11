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

    k = len(points[0])
    axis = depth % k

    points.sort(key=lambda x: x[axis])
    median = len(points) // 2

    return KDTreeNode(
        point=points[median],
        left=build_kd_tree(points[:median], depth + 1),
        right=build_kd_tree(points[median + 1:], depth + 1)
    )

def range_search_kd_tree(node, range_rect, depth=0):
    if node is None:
        return []

    k = len(node.point)
    axis = depth % k

    points_in_range = []
    if (range_rect[0][0] <= node.point[0] <= range_rect[1][0] and
        range_rect[0][1] <= node.point[1] <= range_rect[1][1]):
        points_in_range.append(node.point)

    if node.left and range_rect[0][axis] <= node.point[axis]:
        points_in_range += range_search_kd_tree(node.left, range_rect, depth + 1)
    if node.right and range_rect[1][axis] >= node.point[axis]:
        points_in_range += range_search_kd_tree(node.right, range_rect, depth + 1)

    return points_in_range

def visualize_kd_tree_with_range(node, range_rect, points_in_range, depth=0, bounds=[(0, 100), (0, 100)], ax=None):
    if node is None:
        return

    k = len(node.point)
    axis = depth % k

    if ax is None:
        fig, ax = plt.subplots(figsize=(8, 8))

    ax.plot(node.point[0], node.point[1], 'ro')

    if axis == 0:
        ax.plot([node.point[0], node.point[0]], bounds[1], 'k-')
        visualize_kd_tree_with_range(node.left, range_rect, points_in_range, depth + 1, [(bounds[0][0], node.point[0]), bounds[1]], ax)
        visualize_kd_tree_with_range(node.right, range_rect, points_in_range, depth + 1, [(node.point[0], bounds[0][1]), bounds[1]], ax)
    else:
        ax.plot(bounds[0], [node.point[1], node.point[1]], 'k-')
        visualize_kd_tree_with_range(node.left, range_rect, points_in_range, depth + 1, [bounds[0], (bounds[1][0], node.point[1])], ax)
        visualize_kd_tree_with_range(node.right, range_rect, points_in_range, depth + 1, [bounds[0], (node.point[1], bounds[1][1])], ax)

    # Highlight points in range
    for point in points_in_range:
        ax.plot(point[0], point[1], 'bo')

    # Draw range rectangle
    rect = plt.Rectangle(range_rect[0], range_rect[1][0] - range_rect[0][0], range_rect[1][1] - range_rect[0][1], linewidth=1, edgecolor='g', facecolor='none')
    ax.add_patch(rect)

    return ax

# Generate 100 random points
points = np.random.rand(100, 2) * 100
points = points.tolist()

# Build KD-Tree
kd_tree = build_kd_tree(points)

# Define the range rectangle (bottom-left and top-right corners)
range_rect = [(20, 20), (60, 60)]

# Perform range search
points_in_range = range_search_kd_tree(kd_tree, range_rect)

# Visualize KD-Tree with range search results
ax = visualize_kd_tree_with_range(kd_tree, range_rect, points_in_range)
plt.xlim(0, 100)
plt.ylim(0, 100)
plt.title("KD-Tree Range Search with 100 Points")
plt.show()

# Output the list of points within the range
print("Points within the range:")
for point in points_in_range:
    print(point)
