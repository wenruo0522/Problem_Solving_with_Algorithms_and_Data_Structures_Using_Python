
def hash(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])
        
    return sum%tablesize



def hash2(astring, tablesize):
    sum = 0
    for pos in range(len(astring)):
        sum = sum + ord(astring[pos])*(pos+1)
        
    return sum%tablesize

print(hash('cat',11))
print(hash2('cat',11))