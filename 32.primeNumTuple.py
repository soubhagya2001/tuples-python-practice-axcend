def isPrime(num: int):
    if num == 0 or num == 1:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True

tuple1 = ()

i = 0
while len(tuple1) < 5:
    if isPrime(i):
        tuple1 += (i,)
    i += 1

print(tuple1)
