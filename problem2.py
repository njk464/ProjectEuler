def fib_sum_even(limit):
    fib = [1,2]
    i = 1
    sum = 2
    while fib[i] < limit:
        fib.append(fib[i]+fib[i-1])
	if (fib[i+1]%2 == 0):
	    sum += fib[i+1]
	i += 1
    return sum

print fib_sum_even(4000000)
