import numpy as np

def solve_coffee_blend():
    """
    Solves how many pounds of each coffee type to blend.
    """
    # Coefficient matrix
    A = np.array([
        [1, 1],
        [8, 6]
    ])

    # Right-hand side vector
    b = np.array([50, 375])

    # Solving the system
    solution = np.linalg.solve(A, b)
    x, y = solution

    return x, y

if __name__ == "__main__":
    coffee_8, coffee_6 = solve_coffee_blend()
    print(f"Pounds of $8 coffee: {coffee_8}")
    print(f"Pounds of $6 coffee: {coffee_6}")

    # Test
    assert abs((coffee_8 + coffee_6) - 50) < 1e-6, "Total weight should be 50 pounds"
    assert abs((8 * coffee_8 + 6 * coffee_6) - 375) < 1e-6, "Total value should be $375"
    print("Test passed!")
