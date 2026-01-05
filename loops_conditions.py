def print_numbers_upto(n):
    for i in range(1, n + 1):
        print(i)


def sum_of_even(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total


def check_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
