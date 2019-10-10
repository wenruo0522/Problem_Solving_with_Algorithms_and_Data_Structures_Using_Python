from pythonds.basic import Stack

rStack = Stack()

def toStr(n, base):
    convertString = "0123456789ABCDEF"
    if n < base:
        return convertString[n]
    else:
        return toStr(n//base, base) + convertString[n%base]
    
def toStr2(n, base): 
    toStr3(n, base)
    res = ""
    while not rStack.isEmpty():
        res += rStack.pop()
    return res

def toStr3(n, base):
    
    convertString = "0123456789ABCDEF"    
    if n < base:
        rStack.push(convertString[n])
    else:
        rStack.push(convertString[n%base])
        toStr3(n//base, base)    
  
print(toStr(1453,16))
print(toStr(10,2))
print(toStr2(1453,16))
print(toStr2(10,2))