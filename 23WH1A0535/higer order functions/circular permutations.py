def are_circular_permutations(alpha, beta):
    if len(alpha) != len(beta):
        return False

    combined = alpha + alpha  # Concatenate alpha with itself

    return beta in combined

# Example usage:
alpha_str = "abcde"
beta_str = "bcdea"

result = are_circular_permutations(alpha_str, beta_str)

if result:
    print(f"{alpha_str} and {beta_str} are circular permutations.")
else:
    print(f"{alpha_str} and {beta_str} are not circular permutations.")
