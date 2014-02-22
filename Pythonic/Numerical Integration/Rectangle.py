# Rectangle rule
# Value of a definite integral

import Func_input as F

def limEnter():
        a = eval(input("lowerLim = "))
        b = eval(input("upperLim = "))
        return a, b

def integral(lowerLim, upperLim):
        h = 0.0001
        i = lowerLim
        val = 0
        while i <= upperLim:
                val += h * F.f(i, deg, coef)
                i += h
        return val

deg = []
coef = []
F.enter(deg, coef)
l, u = limEnter()
print("integral value is : ", integral(l, u))