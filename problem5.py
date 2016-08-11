def divis(num):
    arr = []
    for i in range(1,num+1):
        for j in arr:
	    if i % j == 0:
	        i /= j
        arr.append(i)
    mult = 1
    for i in arr:
        mult *= i
    return mult

print divis(20)
