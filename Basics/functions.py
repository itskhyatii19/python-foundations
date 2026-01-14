def add(a, b):
    return a + b


def is_even(number):
    return number % 2 == 0


def find_max(numbers):
    max_val = numbers[0]
    for num in numbers:
        if num > max_val:
            max_val = num
    return max_val
