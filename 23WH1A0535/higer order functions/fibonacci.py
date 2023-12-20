fibonacci = lambda n: [0, 1] if n == 2 else fibonacci(n-1) + [fibonacci(n-1)[-1] + fibonacci(n-1)[-2]]

n = int(input("Enter the value of n: "))
result = fibonacci(n)
print(f"Fibonacci series up to {n}: {result}")
