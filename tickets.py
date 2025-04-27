import numpy as np

def solve_ticket_sales():
    """
    Solves the number of adult and student tickets sold.
    """
    # Coefficient matrix
    A = np.array([
        [1, 1],
        [25, 15]
    ])

    # Right-hand side vector
    b = np.array([120, 2400])

    # Solving the system
    solution = np.linalg.solve(A, b)
    x, y = solution

    return int(x), int(y)

if __name__ == "__main__":
    adult_tickets, student_tickets = solve_ticket_sales()
    print(f"Adult tickets sold: {adult_tickets}")
    print(f"Student tickets sold: {student_tickets}")

    # Test
    assert adult_tickets + student_tickets == 120, "Total tickets should be 120"
    assert 25 * adult_tickets + 15 * student_tickets == 2400, "Total revenue should be $2400"
    print("Test passed!")
