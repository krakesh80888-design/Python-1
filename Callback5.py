numbers = [1, 2, 3, 4, 5]

squared_numbers = list(
    map(lambda x: x * x, numbers)
)
print("Squared numbers:", squared_numbers)

def is_even(num):
    return num % 2 == 0

even_numbers = list(
    filter(is_even, numbers)
)
print("Even numbers:", even_numbers)