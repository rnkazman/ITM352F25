def find_prime_factors(n):
    """
    Find all prime factors of a given integer using integer factorization.
    
    Args:
        n (int): The integer to factorize (must be positive)
    
    Returns:
        list: A list of prime factors in ascending order
    
    Raises:
        ValueError: If n is not a positive integer
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    if n == 1:
        return []
    
    factors = []
    
    # Check for factor 2
    while n % 2 == 0:
        factors.append(2)
        n = n // 2
    
    # Check for odd factors from 3 onwards
    factor = 3
    while factor * factor <= n:
        while n % factor == 0:
            factors.append(factor)
            n = n // factor
        factor += 2
    
    # If n is still greater than 1, then it's a prime factor
    if n > 1:
        factors.append(n)
    
    return factors


def find_prime_factors_with_powers(n):
    """
    Find prime factors with their powers (exponents).
    
    Args:
        n (int): The integer to factorize (must be positive)
    
    Returns:
        dict: A dictionary where keys are prime factors and values are their powers
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("Input must be a positive integer")
    
    if n == 1:
        return {}
    
    factors = {}
    
    # Check for factor 2
    if n % 2 == 0:
        factors[2] = 0
        while n % 2 == 0:
            factors[2] += 1
            n = n // 2
    
    # Check for odd factors from 3 onwards
    factor = 3
    while factor * factor <= n:
        if n % factor == 0:
            factors[factor] = 0
            while n % factor == 0:
                factors[factor] += 1
                n = n // factor
        factor += 2
    
    # If n is still greater than 1, then it's a prime factor
    if n > 1:
        factors[n] = 1
    
    return factors


# Example usage and testing
if __name__ == "__main__":
    # Test cases
    test_numbers = [12, 15, 17, 100, 97, 1, 2, 3, 4, 60]
    
    print("Prime Factorization Examples:")
    print("=" * 40)
    
    for num in test_numbers:
        try:
            factors = find_prime_factors(num)
            factors_with_powers = find_prime_factors_with_powers(num)
            
            print(f"\nNumber: {num}")
            print(f"Prime factors: {factors}")
            print(f"Prime factors with powers: {factors_with_powers}")
            
            # Verify the factorization
            if factors:
                product = 1
                for factor in factors:
                    product *= factor
                print(f"Verification: {' × '.join(map(str, factors))} = {product}")
            else:
                print("Verification: 1 has no prime factors")
                
        except ValueError as e:
            print(f"Error for {num}: {e}")