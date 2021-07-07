"""
Trying the stretch goal of finding whether or not a number is prime
"""
# Prime numbers can only be divided by 1 and itself
# Even numbers are not prime -> odd numbers are prime
# 1 is not a prime number
# If it is not divisible by 2, 3, 5, or 7 then it must be prime.
# All non-prime numbers greater than those numbers can be made using those numbers (F.T.A.)


import sys


simple_primes = [2, 3, 5, 7]

def is_prime(x):
    if x == 1:
        return f'{x} is not a prime number!'
    if x in simple_primes:
        return f'{x} is a prime number.'
    if x % 2 == 0:
        return f'{x} is not a prime number.'
    for i in simple_primes:
        if x % i == 0:
            return f'{x} is not a prime number.'
        elif i == 7:
            return f'{x} is a prime number'

            
if len(sys.argv) <= 1:
    print('Please enter numbers after the call to run the script')
else:
    for i in range(1, len(sys.argv)):
        print(is_prime(int(sys.argv[i])))
        