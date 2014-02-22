# Simpson's 3/8th rule
#  
# Putting n=3 in Newton-Cotes Quadrature formula 
# assuming the curve through (x0, y0) & (x1, y1) as a poly. of 3rd order
#
# Int[F(x)] form (x0) to (x0 + 3h) = (3h/8) [ (y0 + yn) + 3 ( y1 + y2 + y4 + y5 + ... + yn-1 ) + 2 ( y3 + y6 + y9 + ... + yn-3 ) ] 
#
# h is step size
# n is number of steps the interval is divided intotaking 2 steps at one time (therefore, n is even ).

import Func_input as F

def limEnter():
        a = eval(input("lowerLim = "))
        b = eval(input("upperLim = "))
        c = eval(input("stepSize = "))
        while(((b-a) / c) % 3 != 0 ):
                c = eval(input("Valid stepSize = "))
        return a, b, c

def simpson38(lowerLim, upperLim, stepSize):
        i = 0
        val = 0
        while lowerLim <= upperLim:
                if i == 0 or i == int((upperLim - lowerLim + 1) / stepSize) :
                        val += F.f(lowerLim, deg, coef)
                elif i%3 == 0:
                        val += 2 * F.f(lowerLim, deg, coef)
                else :
                        val += 3 * F.f(lowerLim, deg, coef)
                lowerLim+=stepSize
                i += 1
        val *= stepSize * 3
        val/=8
        return val

deg = []
coef = []
F.enter(deg, coef)
l, u, h = limEnter()
print("integral value is : ", simpson38(l, u, h))

