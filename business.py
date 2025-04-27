import numpy as np

def solve_business_production():
    """
    Solves the number of items A, B, and C to produce.
    Assumed labor and material requirements:
        - A: 2 hours labor, 1 material
        - B: 3 hours labor, 2 materials
        - C: 1 hour labor, 3 materials
    """
    # Coefficient matrix
    A = np.array([
        [1, 1, 1],
        [2, 3, 1],
        [1, 2, 3]
    ])

    # Right-hand side vector
    b = np.array([100, 300, 190])

    # Solving the system
    solution = np.linalg.solve(A, b)
    x, y, z = solution

    return int(x), int(y), int(z)

if __name__ == "__main__":
    item_A, item_B, item_C = solve_business_production()
    print(f"Item A: {item_A}")
    print(f"Item B: {item_B}")
    print(f"Item C: {item_C}")

    # Test
    assert item_A + item_B + item_C == 100, "Total items should be 100"
    assert 2 * item_A + 3 * item_B + 1 * item_C == 300, "Total labor should be 300 hours"
    assert 1 * item_A + 2 * item_B + 3 * item_C == 190, "Total materials should be 190 units"
    print("Test passed!")
