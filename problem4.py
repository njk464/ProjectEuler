def is_palindrome(n):
    n = str(n)
    i = 0
    j = len(n)-1
    while i < j:
        if n[i] != n[j]:
	    return False
	i += 1
	j -= 1
    return True


big_p = 0
print is_palindrome(1)

for i in range(100, 1000):
    for j in range(100, 1000):
        k = i*j
	if is_palindrome(k) and k > big_p:
	    big_p = k

print big_p

