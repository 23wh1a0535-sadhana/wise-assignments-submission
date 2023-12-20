#Given two strings alpha and beta check if they are circular permutations of each other. 
#For example: "abcde" and "bcdea" are circular permutations, while "abcde" and "abdce" are NOT 
#Note: The problems in this list are from a range of topics. 
#They should be understood clearly and used when you need a filler or a "Wow! Thats kewl!!" reaction.

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
