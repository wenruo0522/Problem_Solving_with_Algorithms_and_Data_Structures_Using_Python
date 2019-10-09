import time

def sumOfN(n):
    
    start = time.time()
    
    theSum = 0
    for i in range(1, n+1):
        theSum += i
    
    end = time.time()
    return theSum, end - start

def sumOfN2(n):
    return (n*(n+1)/2)

print("Sum is %d required %15.11f seconds" % sumOfN(100000))
print("Sum is %d required %15.11f seconds" % sumOfN(100000000))



        







