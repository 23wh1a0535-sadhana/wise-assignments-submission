#Given a list of non negative integers, write a function which returns the largest number formed by arranging the elements in the list.

def largest_number(nums):
    # Convert integers to strings and sort based on custom comparison
    nums_str = [str(num) for num in nums]
    nums_str.sort(key=lambda x: x * 3, reverse=True)  # Custom comparison for sorting

    # Join the sorted strings to form the largest number
    result = ''.join(nums_str)

    # Remove leading zeros, if any
    result = result.lstrip('0')

    # If the result is empty, return '0'
    return result if result else '0'

# Example usage:
numbers = [3, 30, 34, 5, 9]
result = largest_number(numbers)
print(result)
