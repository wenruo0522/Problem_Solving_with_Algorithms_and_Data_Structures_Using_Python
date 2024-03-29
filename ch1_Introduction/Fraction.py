
class Fraction:
    
    def __init__(self,top,bottom):
        self.num = top
        self.den = bottom
        
    def show(self):
        print(self.num,"/",self.den)
        
    def __str__(self):
        return str(self.num) + "/" + str(self.den)
    
    def __add__(self,otherfraction):
        
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den*otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)
    
    def __eq__(self,other):
        
        firstnum = self.num*other.den
        secondnum = self.den*other.num
        return firstnum == secondnum
        
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n
        
        m = oldn
        n = oldm%oldn
    return n

myf = Fraction(3,5)
myf.show()
print(myf)

f1 = Fraction(1,2)
f2 = Fraction(1,4)
print(f1+f2)











