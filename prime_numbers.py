# prime_numbers.py
# This program prints all prime numbers in a given range.

def is_prime(n):
    """Check if a number is prime."""
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def print_primes_in_range(start, end):
    """Print prime numbers within a given range."""
    print(f"Prime numbers between {start} and {end}:")
    for num in range(start, end + 1):
        if is_prime(num):
            print(num, end=" ")
    print()

# Example usage
print_primes_in_range(10, 50)
