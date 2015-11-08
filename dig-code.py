def digadd(n):
    num_ref = [9,1,2,3,4,5,6,7,8]
    if n > 0:
        results = num_ref[n % 9]
    else:
        results = 0
    return results
    
print digadd(n)
