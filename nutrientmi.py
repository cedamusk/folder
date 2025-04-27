import numpy as np

def solve_nutrient_mix():
    """
    Solves the amount of each ingredient to create a nutrient mix.
    Assumption: All ingredients contribute equally to total protein.
    """
    # Coefficient matrix
    A = np.array([
        [1, 1, 1, 1],
        [1, -2, 0, 0],
        [0, 0, 1, -1]
    ])

    # Right-hand side vector
    b = np.array([100, 0, 0])

    # Solving the system with least squares because underdetermined (infinite solutions)
    solution = np.linalg.lstsq(A, b, rcond=None)[0]
    a, b_, c, d = solution

    return a, b_, c, d

if __name__ == "__main__":
    a, b, c, d = solve_nutrient_mix()
    print(f"Ingredient A: {a:.2f} units")
    print(f"Ingredient B: {b:.2f} units")
    print(f"Ingredient C: {c:.2f} units")
    print(f"Ingredient D: {d:.2f} units")

    # Test
    assert abs((a + b + c + d) - 100) < 1e-6, "Total weight should be 100 units"
    assert abs(a - 2*b) < 1e-6, "Ingredient A should be twice Ingredient B"
    assert abs(c - d) < 1e-6, "Ingredient C and D should be equal"
    print("Test passed!")
