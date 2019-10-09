
class Fraction:
    
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom
        if isinstance(self.num,int) and isinstance(self.den,int):
            pass
        else:
            raise RuntimeError("Please input integer!")
        
    def show(self):
        print(self.num,"/",self.den)
        
    def getNum(self):
        print(self.num)
        
    def getDen(self):
        print(self.den)    
        
    def __str__(self):
        common = gcd(self.num,self.den)
        return str(self.num//common) + "/" + str(self.den//common)
    
    def __add__(self,otherfraction):
        
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den*otherfraction.den
        # common = gcd(newnum,newden)
        # return Fraction(newnum//common,newden//common)
        return Fraction(newnum,newden)
    
    def __sub__(self,otherfraction):
        newnum = self.num*otherfraction.den - self.den*otherfraction.num
        newden = self.den*otherfraction.den
        return Fraction(newnum,newden)        
    
    def __mul__(self,otherfraction):
        newnum = self.num*otherfraction.num 
        newden = self.den*otherfraction.den
        return Fraction(newnum,newden)    
    
    def __truediv__(self,otherfraction):
        if otherfraction.num == 0:
            raise RuntimeError("ATTENTION!")
        else:
            newnum = self.num*otherfraction.den 
            newden = self.den*otherfraction.num
            if newnum % newden == 0:
                return int(newnum//newden)
            else:
                return Fraction(newnum,newden)      
    
    
    def __eq__(self,other):
        
        firstnum == self.num*other.den
        secondnum == self.den*other.num
        return firstnum == secondnum
        
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n
        
        m = oldn
        n = oldm%oldn
    return n

myf = Fraction(3,5)
myf.getNum()
myf.getDen()
myf.show()
print(myf)

f1 = Fraction(1,2)
f2 = Fraction(1,4)
f3 = Fraction(-1,2)
f4 = Fraction(2,5)
print(f1+f2)
print(f3-f2)
print(f1*f4)
print(f1/f2)
f5 = Fraction(2.5,5)
print(f5)











