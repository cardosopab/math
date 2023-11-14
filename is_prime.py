def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n // 2 + 1):
        if n % i == 0:
            return False
    return True


def count_prime_range(start, stop):
    count = 0
    for i in range(start, stop + 1):
        if is_prime(i):
            count += 1
    return count


print(count_prime_range(30, 50))
