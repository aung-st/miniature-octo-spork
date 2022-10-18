from math import sqrt,log

#params
x = 1
y = 1/12
p = x*((x**2) - 5)

function = x+((y*p)*(x**2 -3))

max_iter = 10

approximations = []
errors = []
alphas = []

for i in range(max_iter):
    print(f'iteration {i}')
    
    #current approximation
    print(f'approx: {function}')
    approximations.append(function)
    
    #current approximation error
    error = abs(function-sqrt(3))
    print(f'error: {error}')
    errors.append(error)

    #plug the result back into function to converge to root
    x = function
    function = x+((y*p)*(x**2 -3))


print('')
print(f'approximation of {sqrt(3)}')
print('')
print(f'approximations: {approximations}')
print('')
print(f'errors {errors}')
print('')

#1st and last iter has N/A order calculation 
alphas.append('N/A')
for i in range(1,len(errors)-1):
    alphas.append(log(errors[i+1]/errors[i])/log(errors[i]/errors[i-1]))
alphas.append('N/A')

print(f'orders {alphas}')

for i in range(len(approximations)):
    print(i,approximations[i],errors[i],alphas[i])
    

