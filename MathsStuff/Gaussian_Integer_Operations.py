def divide_GI(a,b,c,d): 
    print(f'{a}+{b}i / {c}+{d}i =')
    f1_n = a*c #R R -> R
    f2_n = a * -d #R I -> I
    f3_n = b*c  # I R -> I
    f4_n = 0 #placeholder
    if b < 0 and d < 0: #-i * -i = i^2 = -1
        f4_n = b*-d
    else:
        f4_n = (b*-d) 
    fr_n = f1_n + f4_n 
    fi_n = f2_n + f3_n 

    denominator  = c**2 + d**2
    
    print(f'{fr_n}/{denominator } + {fi_n}i/{denominator }') 
    

    quotient_r = 0 #placeholder
    quotient_i =0
    remainder_i = 0
    remainder_r = 0
    if fr_n < 0:
        quotient_r = -fr_n // (denominator )
        remainder_r = -fr_n % (denominator )
        remainder_r = -remainder_r
    else:
        quotient_r = fr_n // (denominator )
        remainder_r = fr_n % (denominator )
    if fi_n <0:
        quotient_i = -fi_n // (denominator )
        remainder_i = -fi_n % (denominator )
        remainder_i = -remainder_i
    else:
        quotient_i = fi_n // (denominator )
        remainder_i = fi_n % (denominator )

    
   
    print(f'quotient: {quotient_r}/{denominator} + {quotient_i}i/{denominator}')
    print(f'remainder: {remainder_r}/{denominator}+{remainder_i}i/{denominator}')
    print(f'x ={a}+{b}i, y = {c}+{d}i')
    print(f'y = xq+r')
    print(f'{c}+{d}i = ({a}+{b}i)({quotient_r}/{denominator}+{quotient_i}i/{denominator})+({remainder_r}/{denominator}+{remainder_i}i/{denominator})')
divide_GI(1,2,3,4)
