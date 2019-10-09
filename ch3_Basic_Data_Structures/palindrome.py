from pythonds.basic import Deque

def palChecker(aString):
    chardeque = Deque()
    stillEqual = True
    
    for ch in aString:
        chardeque.addFront(ch)
    
        
    while chardeque.size() > 1 and stillEqual:
        first = chardeque.removeFront()
        last = chardeque.removeRear()
        if  first != last:
            stillEqual = False
    
    return stillEqual    
            

print(palChecker("lsdkjfskf"))
print(palChecker("radar"))
        
    
    

