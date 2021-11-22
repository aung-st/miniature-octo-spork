import numpy
from sympy import Symbol


#Initialize x
x = Symbol('x')
#Function f
#f = x**2-4*x-5
f = x*2 + 1
def NR (f,x0,df=f.diff(x),tolerance=1e-6,max_iterations = 1000):
    initial_value = x0
    counter = 0
    #df.evalf(subs= {x:0})
 
    while not abs(f.evalf(subs = {x:x0})) < tolerance:
        if counter == max_iterations:
            break
        counter +=1
        x0 = x0 - numpy.float(f.evalf(subs = {x:x0})) / numpy.float(df.evalf(subs = {x:x0}))  #NR formula
        print(f'iteration {counter} of x0 is {x0:.3} and f(xn) is {numpy.float(f.evalf(subs= {x:x0})):.3}')
    
    if abs(f.evalf(subs = {x:x0})) < tolerance:
        print(f'approximation of a root at initial value {initial_value} is {x0:.3} after {counter} iterations')

NR(f,6)
