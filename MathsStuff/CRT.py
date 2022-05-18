
def CRT(a,b,c,d,e,f):
    print("= denotes congruent to where the mod is involved. Don't shoot me plz")
    print(f'x = {a} mod {b}')
    print(f'x = {c} mod {d}')
    print(f'x = {e} mod {f}')
    

    N = b*d*f 
    print(f'\nN = n_1 x n_2 x n_3 = {N} where n_1 = {b}, n_2 = {d}, n_3 = {f}')
    print(f'N_i = N/n_i')
    print(f'x_i is given by taking N_i * x = 1 mod n_i and eliminating N_i from the lhs')
    print('\n')
    inv(d*f,b)
    print('\n')
    inv(b*f,d)
    print('\n')
    inv(b*d,f)
    print('\n')

    print('-----------------------------------------------------')
    print('b_i            N_i      x_i       b_i * N_i * x_i')
    print('-----------------------------------------------------')
    print(f'{a}          {d*f}           {inv(d*f,b,False)}              {a*d*f*inv(d*f,b,False)}')
    print(f'{c}          {b*f}           {inv(b*f,d,False)}              {c*b*f*inv(b*f,d,False)}')
    print(f'{e}          {b*d}           {inv(b*d,f,False)}              {e*b*d*inv(b*d,f,False)}')
    
    
    sum_bnx = (a*d*f*inv(d*f,b,False)) + (c*b*f*inv(b*f,d,False)) + (e*b*d*inv(b*d,f,False))
    print(f'\nThe sum of all b_i * N_i * x_i is: {sum_bnx}')
    print(f'x = {sum_bnx} mod {N}')
    print(f'x = {sum_bnx%N} mod {N}')

    print(f'\nThus if we let x = {sum_bnx%N} in the system of linear congruences then the following will hold')
    print(f'{sum_bnx%N} = {a} mod {b}')
    print(f'{sum_bnx%N} = {c} mod {d}')
    print(f'{sum_bnx%N} = {e} mod {f}')

    print(f'\nSo x = {sum_bnx%N} + {N}k')
  
def inv(n,m,show_working=True):
    if show_working:
        print(f'{n}x = 1 mod {m}')
    n%=m

    if show_working:
        print(f'{n}x = 1 mod {m}')
    
    multiplier = 2
    initial = n
    while n%m != 1:
        n = initial
        n *= multiplier 
        n %= m
        multiplier += 1 
    if show_working:
        print(f'x = {multiplier-1} mod {m}')

    return multiplier-1



CRT(3,7,11,22,5,153)
