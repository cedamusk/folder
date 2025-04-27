import numpy as np

def solve_investment_portfolio():
    """
    Solves the distribution of investment in savings, bonds, and stocks.
    """
    # Coefficient matrix
    A = np.array([
        [1, 1, 1],
        [1, -2, 0],
        [0, -1, 1]
    ])

    # Right-hand side vector
    b = np.array([20000, 0, 3000])

    # Solving the system
    solution = np.linalg.solve(A, b)
    x, y, z = solution

    return int(x), int(y), int(z)

if __name__ == "__main__":
    savings, bonds, stocks = solve_investment_portfolio()
    print(f"Savings investment: ${savings}")
    print(f"Bonds investment: ${bonds}")
    print(f"Stocks investment: ${stocks}")

    # Test
    assert savings + bonds + stocks == 20000, "Total investment should be $20,000"
    assert savings == 2 * bonds, "Savings should be twice the bonds"
    assert stocks == bonds + 3000, "Stocks should be $3000 more than bonds"
    print("Test passed!")
