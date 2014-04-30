# Boole's rule
#  
# Putting n=4 in Newton-Cotes Quadrature formula 
# assuming the curve through (x0, y0) & (x1, y1) as a poly. of 4th order
#
# Int[F(x)] form (x0) to (x0 + 4h) = (2*h/45) [ 7*(y0 + yn) + 32*( y1 + y3 + y5 + ... + yn-1 ) + 14*( y4 + y8 + y12 + ... + yn-4 ) +
#  12*( y2 + y6 + ... + yn-2 ) ] 
# h is step size
# n is number of steps the interval is divided into taking 1 step at 1 timeself.

import Func_input as F

def limEnter():
        a = eval(input("lowerLim = "))
        b = eval(input("upperLim = "))
        c = eval(input("stepSize = "))
        while(((b-a) / c) % 4 != 0 ):
                c = eval(input("Valid stepSize = "))
        return a, b, c

def boole(lowerLim, upperLim, stepSize):
        i = 0
        val = 0
        while lowerLim <= upperLim:
                if i == 0 or i == int((upperLim - lowerLim + 1) / stepSize) :
                        val += 7 * F.f(lowerLim, deg, coef)
                elif i%4 == 0:
                        val += 14 * F.f(lowerLim, deg, coef)
                elif i%2 == 0:
                        val += 12 * F.f(lowerLim, deg, coef)
                else :
                        val += 32 * F.f(lowerLim, deg, coef)
                lowerLim += stepSize
                i += 1
        val *= stepSize * 2
        val/=45
        return val

if __name__ == '__main__':
        deg = []
        coef = []
        F.enter(deg, coef)
        l, u, h = limEnter()
        print("integral value is : ", boole(l, u, h))