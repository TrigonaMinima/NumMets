# Gauss Elimination method

import function.linear as fun

def GaussEli( size, mat ):
        '''
        Takes in the coefficient matrix and size and returns the list of solutions.
        '''
        for k in range(size-1):
                for i in range(k+1, size):
                        print(mat[i][k], mat[k][k])
                        print(mat)
                        alpha = mat[i][k] / mat[k][k]
                        for j in range(k, size+1):
                                mat[i][j] -= mat[k][j] * alpha
        sol = [ 0 for x in range(size) ]
        for i in reversed(range(size)):
                val = mat[i][size-1]
                for j in reversed(range(size-i-1)):
                        if j==0:
                                val/=mat[i][j]
                        else:
                                val -= sol[j] * mat[i][j]
                sol[i] = val
        return sol

if __name__ == '__main__':
        a, mat = fun.eq()
        print(mat)
        print(GaussEli(a, mat))
