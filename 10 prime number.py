# Program to print the first 10 prime numbers

primes = []
num = 2  # Start from the first prime number

while len(primes) < 10:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        primes.append(num)
    num += 1

print("First 10 prime numbers:", primes)
