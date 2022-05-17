def divide_GI(x,y,z,w): 
    print(f'({z}+{w}i) / ({x}+{y}i) =')
    #Multiply both numerator and denominator by conjugate
    print(f'({z}+{w}i)({x}-{y}i) / ({x}+{y}i)({x}-{y}i) =')
    
    #Apply foil (Very messy I know...)
    f1 = z * x
    fi = (w*x) + (z*-y) 
    f3 = None # placeholder
    

    if w < 0 and y<0: # -i * i = -i^2 = 1
        f3 = -w*y
    else: #i * i = i^2 = -1 
        f3 = -1 * (-w)*y 
    
    fr = f1 + f3 
    denominator  = x**2 + y**2
    quotient_r = None 
    quotient_i = None 

    if fi < 0:
        quotient_i= -fi//denominator
        quotient_i = -quotient_i
    else:
        quotient_i= fi//denominator
    
    if fr < 0:
        quotient_r= -fr//denominator
        quotient_r = -quotient_r
    else:
        quotient_r= fr//denominator
    
    
    print(f'{fr}/{denominator } + {fi}i/{denominator } =') 
    print(f'{fr/denominator} + {fi/denominator}i \n')
    print(f'quotient: {quotient_r} + {quotient_i}i')
    print('b = aq + r \n')
    print('r = b - aq')
    print(f'r = ({z}+{w}i) - ({x}+{y}i)({quotient_r}+{quotient_i}i)')

    #Apply foil again (Don't hang me plz...)
    f1 = quotient_r * x
    fi = (quotient_i*x) + (quotient_r*y) 
    f3 = None # placeholder

  
    if w < 0 and y<0: # -i * i = -i^2 = 1
        f3 = quotient_i*y
    else: #i * i = i^2 = -1 
        f3 = -1 * (quotient_i)*y  
    
    fr = f1 + f3 
    
    print(f'r = ({z}+{w}i) - ({fr}+{fi}i)')
    print(f'r = ({z-fr}+{w-fi}i) \n')
    print('b = aq + r =')
    print(f'({z}+{w}i) = ({x}+{y}i)({quotient_r}+{quotient_i}i) + ({z-fr}+{w-fi}i)') 

divide_GI(1,2,3,4)

