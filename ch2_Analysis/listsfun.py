import timeit

def test1():
    li = []
    for i in range(1000):
        li = li + [i]
        
def test2():
    li = []
    for i in range(1000):
        li.append(i)
        
def test3():
    li = [i for i in range(1000)]
    
def test4():
    li = list(range(1000))
    
    
t1 = timeit.Timer("test1()", "from __main__ import test1")
print("concat ",t1.timeit(number=1000), "milliseconds")

t2 = timeit.Timer("test2()", "from __main__ import test2")
print("append ",t2.timeit(number=1000), "milliseconds")

t3 = timeit.Timer("test3()", "from __main__ import test3")
print("comprehension ",t3.timeit(number=1000), "milliseconds")

t4 = timeit.Timer("test4()", "from __main__ import test4")
print("list range ",t4.timeit(number=1000), "milliseconds")

t5 = timeit.Timer()
print("empty call_function ",t5.timeit(number=1000), "milliseconds")

    
    
    

























