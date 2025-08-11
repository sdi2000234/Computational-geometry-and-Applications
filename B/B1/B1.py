import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import linprog

# Function to generate random constraints
def generate_random_constraints(num_constraints):
    np.random.seed(42)
    A = np.random.rand(num_constraints, 2)
    b = np.random.rand(num_constraints)
    return A, b

# Function to solve the linear programming problem using the incremental algorithm
def incremental_lp(A, b, c):
    num_constraints = A.shape[0]
    best_solution = None
    best_value = float('inf')
    
    for i in range(num_constraints):
        A_subset = A[:i+1]
        b_subset = b[:i+1]
        res = linprog(c, A_ub=A_subset, b_ub=b_subset, method='highs')
        
        if res.success and res.fun < best_value:
            best_solution = res.x
            best_value = res.fun
    
    return best_solution, best_value

# Function to visualize the feasible region and the optimal solution
def visualize_lp(A, b, c, solution):
    x = np.linspace(0, 1, 400)
    y = np.linspace(0, 1, 400)
    X, Y = np.meshgrid(x, y)
    
    plt.figure(figsize=(8, 8))
    
    for i in range(A.shape[0]):
        plt.fill_between(x, 0, b[i] / A[i, 1] - (A[i, 0] / A[i, 1]) * x, alpha=0.3)
    
    if solution is not None:
        plt.plot(solution[0], solution[1], 'ro', label='Optimal Solution')
    
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Feasible Region and Optimal Solution')
    plt.legend()
    plt.show()

# Generate random constraints
num_constraints = 5
A, b = generate_random_constraints(num_constraints)

# Define the objective function
c = np.array([-1, -1])

# Solve the linear programming problem using the incremental algorithm
solution, value = incremental_lp(A, b, c)

# Visualize the feasible region and the optimal solution
visualize_lp(A, b, c, solution)
