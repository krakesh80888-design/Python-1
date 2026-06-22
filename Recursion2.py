def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci sequence up to 6:",
      [fibonacci(i) for i in range(7)])