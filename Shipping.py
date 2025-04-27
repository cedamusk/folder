import numpy as np

def solve_shipping_optimization():
    """
    Solves the shipping allocation across truck, rail, air, and ship.
    """
    # Coefficient matrix
    A = np.array([
        [1, 1, 1, 1],
        [1, -1, 0, 0],
        [-1, -1, 1, 0],
        [0, 0, -3, 1]
    ])

    # Right-hand side vector
    b = np.array([1000, 0, -200, 0])

    # Solving the system
    solution = np.linalg.solve(A, b)
    x, y, z, w = solution

    return int(x), int(y), int(z), int(w)

if __name__ == "__main__":
    truck, rail, air, ship = solve_shipping_optimization()
    print(f"Truck: {truck} tons")
    print(f"Rail: {rail} tons")
    print(f"Air: {air} tons")
    print(f"Ship: {ship} tons")

    # Test
    assert truck + rail + air + ship == 1000, "Total shipment should be 1000 tons"
    assert truck == rail, "Truck and rail amounts should be equal"
    assert air == (truck + rail) - 200, "Air should be combined truck and rail minus 200"
    assert ship == 3 * air, "Ship should carry three times the air shipment"
    print("Test passed!")