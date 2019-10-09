
from pythonds.basic import Stack

def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol == "(":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                s.pop()
        index += 1
        
    if balanced and s.isEmpty():
        return True
    else:
        return False
    

def parChecker2(symbolString):
    
    s = Stack()
    balanced = True
    index = 0
    
    while index < len(symbolString) and balanced:
        symbol = symbolString[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.isEmpty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top,symbol):
                    balanced = False 
        index += 1
        
    if balanced and s.isEmpty():
        return True
    else:
        return False
    
    
def matches(left, right):
    lefts = "([{"
    rights = ")]}"
    
    return lefts.index(left) == rights.index(right)

print(parChecker('((()))'))
print(parChecker('(()'))
        
print(parChecker2('{({([][])}())}'))
print(parChecker2('[{()]'))








