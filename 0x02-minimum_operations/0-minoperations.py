def minOperations(n):
    if n <= 1:
        return 0

    operations = 0
    div = 2

    while n > 1:
        if n % div == 0:
            n //= div
            operations += div
        else:
            div += 1

    return operations
