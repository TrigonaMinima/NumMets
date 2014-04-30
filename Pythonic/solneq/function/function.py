# Functions to get a polynomial from the user

# Displays the polynomial
def disp(deg, coef):
        i = 1
        print(str(coef[0]) + " * x^" + str(deg[0]), end='')
        for i in range(1,len(deg)):
                if len(deg) == 1:
                        break
                print(" + ", end='')
                print(str(coef[i]) + " * x^" + str(deg[i]), end='' )
        print()

def enter( deg, coef):
        a = input("Enter degree of 1st term : ")
        deg.append(eval(a))
        a = input("Enter coefficient of 1st term : ")
        coef.append(eval(a))
        while 1:
                a = input("Enter degree of next term : ")
                if a == '':
                        break
                deg.append(eval(a))
                a = input("Enter coefficient of the present term : ")
                coef.append(eval(a))
        print("Your func is : ")
        disp(deg, coef)
        return None

def f(num, deg, coef):
        sum = 0
        i = 0
        for i in range(len(deg)):
                sum += coef[i] * (num ** deg[i])
                i+=1
        return sum