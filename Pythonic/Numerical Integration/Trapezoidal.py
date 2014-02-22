# Trapezoidal rule
#  
# Putting n=1 in Newton-Cotes Quadrature formula 
# assuming the curve through (x0, y0) & (x1, y1) as a straight line i.e a poly. of 1st order
#
# Int[F(x)] form (x0) to (x0 + h) = (h/2) [ (y0 + yn) + 2 ( y1 + y2 + y3 + ... + yn-1 ) ] 
#
# h is step size
# n is number of steps the interval is divided into taking 1 step at 1 time.

import Func_input as F

def limEnter():
        a = eval(input("lowerLim = "))
        b = eval(input("upperLim = "))
        c = eval(input("stepSize = "))
        return a, b, c

def trapezoidal(lowerLim, upperLim, stepSize):
        i = 0
        val = 0
        while lowerLim <= upperLim:
                if i == 0 or i == upperLim/stepSize :
                        val += F.f(lowerLim, deg, coef)
                else:
                        val += 2 * F.f(lowerLim, deg, coef)
                lowerLim+=stepSize
                i += 1
        val *= stepSize
        val/=2
        return val

deg = []
coef = []
F.enter(deg, coef)
l, u, h = limEnter()
print("integral value is : ", trapezoidal(l, u, h))

