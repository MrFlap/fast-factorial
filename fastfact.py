import functools
import time
import math

def digitCount(n):
    return int(math.log(n, 10))
    
def cumulativeFactors(f, n):
    ans = 0
    while n > 1:
        n = n // f
        ans += n
    return ans

def sieveOfEratosthenes(n):
    if n < 2: return None
    if n == 2: return [2]
    numbers = [True for i in range(n - 1)]
    for i in range(0, int(n**.5) + 1):
        if numbers[i]:
            j = (i + 2) * (i + 2)
            while j <= n:
                numbers[j - 2] = False
                j += i + 2
    number_list = []
    for i in range(len(numbers)):
        if numbers[i]: number_list.append(i + 2)
    return number_list

def primeFactorizeFactorial(n):
    primes = sieveOfEratosthenes(n)
    print([n//i for i in primes])
    repetitions = [cumulativeFactors(i, n) for i in primes]
    return(primes, repetitions)
    # ans = []
    # for i in range(len(primes)):
        # ans.extend([primes[i] for j in range(repetitions[i])])
    # return ans

def ffact2(n):
    primes = sieveOfEratosthenes(n)
    ans = 1
    for i in range(len(primes)):
        ans *= primes[i] ** cumulativeFactors(primes[i], n)
    return ans
    
def factorialSolve(n):
    primes, repetitions = primeFactorizeFactorial(n)
    ans = 1
    for i in range(len(primes)):
        ans *= primes[i] ** repetitions[i]
    return ans

def slowFactorial(n):
    ans = 1
    for i in range(2, n + 1):
        ans *= i
    return ans
    
counter = time.time()
print("CALCULATION TIME FOR 100,000! USING FAST ALGORITHM:")
fast = ffact2(100000)
print(time.time() - counter)
print("DIGITS: ", digitCount(fast))
counter = time.time()
print("CALCULATION TIME FOR 100,000! USING NAIVE APPROACH:")
slow = slowFactorial(100000)
print(time.time() - counter)
print("DIGITS: ", digitCount(slow))