import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Define the constraints
A = np.array([
    [-1, 2],
    [-2, 3],
    [1, -3],
    [1, -6],
    [-4, 9]
])

b = np.array([-1, -6, 0, 12, 27])

# Define the objective function
c = np.array([3, -12])

# Function to solve the linear programming problem using the incremental algorithm
def incremental_lp(A, b, c):
    num_constraints = A.shape[0]
    best_solution = None
    best_value = -float('inf')
    
    for i in range(num_constraints):
        A_subset = A[:i+1]
        b_subset = b[:i+1]
        res = linprog(-c, A_ub=A_subset, b_ub=b_subset, bounds=(0, None), method='highs')
        
        if res.success and res.fun > best_value:
            best_solution = res.x
            best_value = res.fun
    
    return best_solution, -best_value

# Function to visualize the feasible region and the optimal solution
def visualize_lp(A, b, c, solution):
    x = np.linspace(0, 15, 400)
    y = np.linspace(0, 15, 400)
    X, Y = np.meshgrid(x, y)
    
    plt.figure(figsize=(8, 8))
    
    for i in range(A.shape[0]):
        if A[i, 1] != 0:
            plt.fill_between(x, 0, b[i] / A[i, 1] - (A[i, 0] / A[i, 1]) * x, alpha=0.3)
        else:
            plt.axvline(x=b[i] / A[i, 0], alpha=0.3)
    
    if solution is not None:
        plt.plot(solution[0], solution[1], 'ro', label='Optimal Solution')
    
    plt.xlim(0, 15)
    plt.ylim(0, 15)
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.title('Feasible Region and Optimal Solution')
    plt.legend()
    plt.show()

# Solve the linear programming problem using the incremental algorithm
solution, value = incremental_lp(A, b, c)

# Print the optimal solution and the value of the objective function
print(f'Optimal Solution: x1 = {solution[0]}, x2 = {solution[1]}')
print(f'Optimal Value: {value}')

# Visualize the feasible region and the optimal solution
visualize_lp(A, b, c, solution)
