#Given a string, write a function to find the rank of the string amongst its permutations sorted lexicographically. 
#Note: Assume that no characters are repeated.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def get_rank(s):
    rank = 1
    n = len(s)

    for i in range(n):
        count = 0
        for j in range(i + 1, n):
            if s[j] < s[i]:
                count += 1

        rank += count * factorial(n - i - 1)

    return rank

# Example usage:
input_string = "STRING"
result_rank = get_rank(input_string)
print(f"The rank of the string '{input_string}' is: {result_rank}")
