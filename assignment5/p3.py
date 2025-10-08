# Define the universe of discourse (the elements)
elements = ['x1', 'x2', 'x3', 'x4', 'x5']

# Define the fuzzy sets P and Q as dictionaries
# The keys are the elements and the values are their membership degrees
P = {'x1': 0.1, 'x2': 0.2, 'x3': 0.7, 'x4': 0.5, 'x5': 0.4}
Q = {'x1': 0.9, 'x2': 0.6, 'x3': 0.3, 'x4': 0.2, 'x5': 0.8}

def lambda_cut(fuzzy_set, lambda_val):
    """
    Calculates the lambda-cut (or alpha-cut) of a fuzzy set.

    Args:
        fuzzy_set (dict): The fuzzy set to operate on.
        lambda_val (float): The lambda (alpha) value for the cut.

    Returns:
        set: A crisp set of elements whose membership is >= lambda_val.
    """
    # Use a set comprehension to find all elements where the membership
    # degree is greater than or equal to the lambda value.
    return {element for element, membership in fuzzy_set.items() if membership >= lambda_val}

def fuzzy_union(set_a, set_b):
    """
    Calculates the union of two fuzzy sets.
    The membership of an element in the union is the max of its memberships in the two sets.

    Args:
        set_a (dict): The first fuzzy set.
        set_b (dict): The second fuzzy set.

    Returns:
        dict: The resulting fuzzy set from the union.
    """
    union_set = {}
    all_elements = set(set_a.keys()) | set(set_b.keys())
    for element in all_elements:
        union_set[element] = max(set_a.get(element, 0), set_b.get(element, 0))
    return union_set

def fuzzy_intersection(set_a, set_b):
    """
    Calculates the intersection of two fuzzy sets.
    The membership of an element in the intersection is the min of its memberships in the two sets.

    Args:
        set_a (dict): The first fuzzy set.
        set_b (dict): The second fuzzy set.

    Returns:
        dict: The resulting fuzzy set from the intersection.
    """
    intersection_set = {}
    all_elements = set(set_a.keys()) & set(set_b.keys()) # Common elements
    for element in all_elements:
        intersection_set[element] = min(set_a.get(element, 0), set_b.get(element, 0))
    return intersection_set

def fuzzy_complement(fuzzy_set):
    """
    Calculates the complement of a fuzzy set.
    The membership of an element in the complement is 1 minus its original membership.

    Args:
        fuzzy_set (dict): The fuzzy set to find the complement of.

    Returns:
        dict: The complement fuzzy set.
    """
    complement_set = {}
    for element, membership in fuzzy_set.items():
        complement_set[element] = 1 - membership
    return complement_set

def main():
    """
    Main function to perform the calculations and print the results.
    """
    print("Fuzzy Sets:")
    print(f"P = {P}")
    print(f"Q = {Q}\n")

    # 1. P_0.2 and Q_0.3
    p_cut_0_2 = lambda_cut(P, 0.2)
    q_cut_0_3 = lambda_cut(Q, 0.3)
    print(f"1. P_0.2 = {sorted(list(p_cut_0_2))}")
    print(f"   Q_0.3 = {sorted(list(q_cut_0_3))}\n")

    # 2. (P U Q)_0.6
    p_union_q = fuzzy_union(P, Q)
    p_union_q_cut_0_6 = lambda_cut(p_union_q, 0.6)
    print(f"   P U Q = {p_union_q}")
    print(f"2. (P U Q)_0.6 = {sorted(list(p_union_q_cut_0_6))}\n")

    # 3. (P U P')_0.8
    p_complement = fuzzy_complement(P)
    p_union_p_complement = fuzzy_union(P, p_complement)
    p_union_p_complement_cut_0_8 = lambda_cut(p_union_p_complement, 0.8)
    print(f"   P' = {p_complement}")
    print(f"   P U P' = {p_union_p_complement}")
    print(f"3. (P U P')_0.8 = {sorted(list(p_union_p_complement_cut_0_8))}\n")

    # 4. (P ∩ Q)_0.4
    p_intersect_q = fuzzy_intersection(P, Q)
    p_intersect_q_cut_0_4 = lambda_cut(p_intersect_q, 0.4)
    print(f"   P ∩ Q = {p_intersect_q}")
    print(f"4. (P ∩ Q)_0.4 = {sorted(list(p_intersect_q_cut_0_4))}\n")

if __name__ == "__main__":
    main()
