import math

def is_prime(n):
    if n == 2 or n == 3: return True
    if n < 2 or n%2 == 0: return False
    if n%3 == 0: return False
    r = int(n**0.5)
    f = 3
    while f < r:
	if n%f == 0: 
	    return False
	f += 2
    return True    


def largest_prime(num):
    n = int((num**0.5))
    i = 1
    big_prime = 1
    while i < n:
    	if num % i == 0 and is_prime(i):
	    big_prime = i
        i += 2
    return big_prime

print largest_prime(20)
print largest_prime(600851475143)
