def prime(n):
    if n < 2:
        return False
    for i in range(2, round(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

prime(61)
prime(10)
