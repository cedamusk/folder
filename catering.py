import numpy as np

def solve_event_catering():
    """
    Solves the number of each meal type ordered for an event.
    """
    # Coefficient matrix
    A = np.array([
        [1, 1, 1, 1, 1],    # Total meals = 500
        [0, 1, 1, 0, 0],    # Vegetarian + Vegan = 200
        [0, 0, 0, 1, -2],   # Kids = 0.5 * Gluten-Free (=> 2k = gf)
        [1, -1, 0, 0, 0],   # Regular = Vegetarian
        [0, 0, 1, -1, 0]    # Vegan = Gluten-Free + 25
    ])

    # Right-hand side vector
    b = np.array([500, 200, 0, 0, 25])

    # Solving
    solution = np.linalg.lstsq(A, b, rcond=None)[0]
    r, v, vg, gf, k = solution

    return r, v, vg, gf, k

if __name__ == "__main__":
    r, v, vg, gf, k = solve_event_catering()
    print(f"Regular Meals: {r:.2f}")
    print(f"Vegetarian Meals: {v:.2f}")
    print(f"Vegan Meals: {vg:.2f}")
    print(f"Gluten-Free Meals: {gf:.2f}")
    print(f"Kids Meals: {k:.2f}")

    # Test
    assert abs((r + v + vg + gf + k) - 500) < 1e-6, "Total meals should be 500"
    assert abs((v + vg) - 200) < 1e-6, "Vegetarian + Vegan should be 200"
    assert abs(gf - 2*k) < 1e-6, "Kids meals should be half Gluten-Free"
    assert abs(r - v) < 1e-6, "Regular meals should equal Vegetarian meals"
    assert abs(vg - (gf + 25)) < 1e-6, "Vegan meals should be Gluten-Free + 25"
    print("Test passed!")
