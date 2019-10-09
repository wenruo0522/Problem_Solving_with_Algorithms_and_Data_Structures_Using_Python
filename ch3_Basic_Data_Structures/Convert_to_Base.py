from pythonds.basic import Stack

def divideBy2(decNumber):
     
     remStack = Stack()
     
     while decNumber > 0 :
          rem = decNumber % 2
          remStack.push(rem)
          decNumber = decNumber//2
     
     binString = ""
     while not remStack.isEmpty():
          binString = binString + str(remStack.pop())
          
     return binString

def baseConverter(decNumber, base):
     
     digits = "0123456789ABCDEF"
     remStack = Stack()
     
     while decNumber > 0 :
          rem = decNumber % base
          remStack.push(rem)
          decNumber = decNumber//base
     
     baseString = ""
     while not remStack.isEmpty():
          baseString = baseString + digits[remStack.pop()]
          
     return baseString     
     

print(divideBy2(42))
print(divideBy2(233))
print(baseConverter(233,8))
print(baseConverter(233,16))
     
          
    





