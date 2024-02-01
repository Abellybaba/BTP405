#def getPrimeNumbers(n):

def is_prime(number):
    """Check if a number is prime."""
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def getPrimeNumbers(n):
    """Return a list of prime numbers from 2 to n."""
    return [x for x in range(2, n + 1) if is_prime(x)]


n = 20  
prime_numbers = getPrimeNumbers(n)
print(f"Prime numbers between 2 and {n}: {prime_numbers}")
