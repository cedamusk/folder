import numpy as np

def solve_marketing_budget():
    """
    Solves the marketing budget allocation among social media, TV ads, and influencer marketing.
    """
    # Coefficient matrix
    A = np.array([
        [1, 1, 1],
        [-1, 1, -1],
        [-2, 0, 1]
    ])

    # Right-hand side vector
    b = np.array([60000, 0, 0])

    # Solving the system
    solution = np.linalg.solve(A, b)
    x, y, z = solution

    return int(x), int(y), int(z)

if __name__ == "__main__":
    social_media, tv_ads, influencer = solve_marketing_budget()
    print(f"Social Media: ${social_media}")
    print(f"TV Ads: ${tv_ads}")
    print(f"Influencer Partnerships: ${influencer}")

    # Test
    assert social_media + tv_ads + influencer == 60000, "Total budget should be $60,000"
    assert tv_ads == social_media + influencer, "TV ads should equal social media + influencer"
    assert influencer == 2 * social_media, "Influencer should be twice social media"
    print("Test passed!")
