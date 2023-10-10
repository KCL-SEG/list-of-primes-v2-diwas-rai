"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""
def primeOrNot(num):
    if num <= 1:
        return False
    
    for i in range(2,num):
        if num % i == 0:
            return False
    
    return True
    

def primes(number_of_primes):
    list = []

    if number_of_primes <= 0:
        raise ValueError(f"Argument passed into primes() was {number_of_primes}. This should be greater than 0")
    
    primesFound = 0
    num = 2

    while primesFound < number_of_primes:
        if primeOrNot(num) == True:
            primesFound += 1
            list.append(num)
        num += 1

    return list