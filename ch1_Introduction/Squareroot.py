
def squareRoot(n):
    root = n/2 # initial guess will be 1/2 of n
    for k in range(20):
        root = (1/2)*(root + n/root)
    return root

print(squareRoot(9))
print(squareRoot(4563))

    

