class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, newdata):
        self.data = newdata
        
    def setNext(self, newnext):
        self.next = newnext
        

class UnorderedList:
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp
        
    
    def length(self):
        count = 0
        current = self.head
        while current != None:
            count += 1
            current = current.getNext()
        return count     
    
    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        
        return found
    
    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            
    def __str__(self):
        result = list()
        
        current = self.head
        while current != None:
            result.append(current.getData())
            current = current.getNext()
        return str(result)
            
            
mylist = UnorderedList()
            
mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print(mylist)         
print(mylist.length())
print(mylist.search(93))
print(mylist.search(100))
            
mylist.add(100)
print(mylist.search(100))
print(mylist.length())
            
mylist.remove(54)
print(mylist.length())
mylist.remove(93)
print(mylist.length())
mylist.remove(31)
print(mylist.length())
print(mylist.search(93))
                






