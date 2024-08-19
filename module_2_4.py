# Всё не так уж просто
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
len_numbers = len(numbers)

for i in range(1, len_numbers):
    is_prime = True
    if numbers[i] == 1: continue
    for ii in range(2, numbers[i]):
        if numbers[i] % ii == 0:
            is_prime = False
            break
    if is_prime == True:
        primes.append(numbers[i])
    else:
        not_primes.append(numbers[i])

print(primes)
print(not_primes)
