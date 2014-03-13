# Iterative formula to find Sq. root

import reciprocal as reci

def root( num ):
        """
        Take a number (int or float) and returns its sq root. If the number given in negative then the function returns none.
        """
        if num < 0:
                print ("A complex number!!")
                return none
        x=num/2;
        while 1 :
                y = (0.5) * ( x + num * reci.reciprocal(x) )
                if ( (int(y*10000000000) - int(x*10000000000)) == 0):
                        return y
                        break
                x = y

#if __name__ == '__main__':
read(n)
print (root(n))
