def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        return False
    return True


def count_prime_range(start, stop):
    count = 0
    for i in range(start, stop + 1):
        if is_prime(i):
            count += 1
    return count


print(count_prime_range(30, 50))
print(count_prime_range(-3, 3))
