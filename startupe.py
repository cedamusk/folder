import numpy as np

def solve_startup_equity():
    """
    Solves the equity distribution among four founders.
    """
    # Coefficient matrix
    A = np.array([
        [1, 1, 1, 1],  # total equity is 100%
        [1, -1, 0, 0],  # a = b + 5
        [0, -2, 1, 0],  # c = 2b
        [1, 1, 0, -1]   # d = (a + b) - 10
    ])

    # Right-hand side vector
    b = np.array([100, 5, 0, -10])

    # Solving
    solution = np.linalg.lstsq(A, b, rcond=None)[0]
    a, b_, c, d = solution

    return a, b_, c, d

if __name__ == "__main__":
    a, b, c, d = solve_startup_equity()
    print(f"Founder A: {a:.2f}% equity")
    print(f"Founder B: {b:.2f}% equity")
    print(f"Founder C: {c:.2f}% equity")
    print(f"Founder D: {d:.2f}% equity")

    # Test
    assert abs((a + b + c + d) - 100) < 1e-6, "Total equity should be 100%"
    assert abs(a - (b + 5)) < 1e-6, "Founder A should have 5% more than Founder B"
    assert abs(c - 2*b) < 1e-6, "Founder C should have twice Founder B's equity"
    assert abs(d - (a + b - 10)) < 1e-6, "Founder D should get (A+B)-10%"
    print("Test passed!")
