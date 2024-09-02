numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

primes = []
not_primes = []

i = 0
for i in range(2,len(numbers)):
    number = 0
    while  number < 2:
        number = numbers[i]
    prime = True
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            prime = False
            break
        prime = True
    if prime:
        primes.append(number)
    else:
        not_primes.append(number)

print('Primes:',primes)
print('Not Primes:',not_primes)