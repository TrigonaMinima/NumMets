# Takes n number of linear equations to be solved 


def disp(size, arr):
        '''
        takes the number of variables and the coefficient matrix and displays the equations as - 
        ax1 + bx2 + cx3 = d
        '''
        print("Your entered equations are -")
        for x in range(size):
                for y in range(size+1):
                        if y==size :
                                print(str(arr[x][y]))
                        else:
                                if y==size-1:
                                        print("(" + str(arr[x][y]) + ") * x" + str(y) + " = ", end='')
                                else:
                                        print("(" + str(arr[x][y]) + ") * x" + str(y) + " + ", end='')
        return None


def eq():
        '''
        returns a the number of variable and list containing the coeffecients and constants
        eg: ax + by + cz = d
        it returns : 3 [ [a, b, c, d] ]
        '''
        a = eval(input("Enter the no of variables : "))
        print("Enter the equations -")
        mat = [[0 for x in range(a+1)] for x in range(a)]
        for x in range(a):
                print("Eq #", x+1)
                for y in range(a+1):
                        mat[x][y] = eval(input("coeffecient/constant : "))
        disp(a, mat)
        return a, mat

if __name__ == '__main__':
        eq()