# Simpson's 1/3rd rule
#  
# Putting n=2 in Newton-Cotes Quadrature formula 
# assuming the curve through (x0, y0) & (x1, y1) as a parabola i.e a poly. of 2nd order
#
# Int[F(x)] form (x0) to (x0 + 2h) = (h/3) [ (y0 + yn) + 4 ( y1 + y3 + y5 + ... + yn-1 ) + 2 ( y2 + y4 + y6 + ... + yn-2 ) ] 
#
# h is step size
# n is number of steps the interval is divided intotaking 2 steps at one time (therefore, n is even ).

import Func_input as F

def limEnter():
        a = eval(input("lowerLim = "))
        b = eval(input("upperLim = "))
        c = eval(input("stepSize = "))
        while(((b-a) / c) % 2 != 0 ):
                c = eval(input("Valid stepSize = "))
        return a, b, c

def simpson13(lowerLim, upperLim, stepSize):
        i = 0
        val = 0
        while lowerLim <= upperLim:
                if i == 0 or i == int((upperLim - lowerLim + 1) / stepSize) :
                        val += F.f(lowerLim, deg, coef)
                elif i%2 == 0:
                        val += 2 * F.f(lowerLim, deg, coef)
                else :
                        val += 4 * F.f(lowerLim, deg, coef)
                lowerLim+=stepSize
                i += 1
        val *= stepSize
        val/=3
        return val

if __name__ == __main__:
        deg = []
        coef = []
        F.enter(deg, coef)
        l, u, h = limEnter()
        print("integral value is : ", simpson13(l, u, h))

