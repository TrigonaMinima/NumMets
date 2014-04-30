# 1. Bisection method 
#               x1 = (a+b)/2
# 2. method of false position
#               x1 = [ a*f(b) - b*f(a) ] / [ f(b) - f(a) ]

import Func_input as F

def initialSol():
        x = -100;
        while x<100:
                if ( F.f(x, deg, coef) * F.f(x+0.5, deg, coef) ) < 0 :
                        if F.f(x, deg, coef) < 0 :
                                return x, x+0.5
                        else :
                                return x+0.5, x
                x+=0.5


def chk(num1, num2):
        if ( (int(num1*(10**6)) - int(num2*(10**6))) == 0 ):
                return 1
        return 0

def bisection():
        x, y = initialSol()
        # print(x, y)
        while 1 :
                temp = (x+y)/2;
                if(F.f(temp, deg, coef) == 0):
                        return temp
                elif (F.f(temp, deg, coef) <  0):
                        if chk(x, temp):
                                return temp
                        x = temp
                else:
                        if chk(y, temp):
                                return temp
                        y = temp

def falPosition():
        x, y = initialSol()
        # print(x, y)
        while 1 :
                temp = (F.f(y, deg, coef) * x - y * F.f(x, deg, coef)) / ( F.f(y, deg, coef) - F.f(x, deg, coef) );
                if(F.f(temp, deg, coef) == 0):
                        return temp
                else:
                        if chk(y, temp):
                                return temp
                        y = temp


deg = []
coef = []
F.enter(deg, coef)
print(deg)
print(coef)
a = bisection()
b = falPosition()
print (a)
print (b)
print(F.f(a, deg, coef))
print(F.f(b, deg, coef))