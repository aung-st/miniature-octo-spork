def CRT(a,b,c,d,e,f):
    print("= denotes congruent to. Don't shoot me plz")
    print(f'x = {a} mod {b}')
    print(f'x = {c} mod {d}')
    print(f'x = {e} mod {f}')
    
    N = b*d*f 
    sum_bnx = (a*d*f*inv(d*f,b)) + (c*b*f*inv(b*f,d)) + (e*b*d*inv(b*d,f))

    print('-----------------------------------------------------')
    print('b_i            N_i      x_i       b_i * N_i * x_i')
    print('-----------------------------------------------------')
    print(f'{a}          {d*f}           {inv(d*f,b)}              {a*d*f*inv(d*f,b)}')
    print(f'{c}          {b*f}           {inv(b*f,d)}              {c*b*f*inv(b*f,d)}')
    print(f'{e}          {b*d}           {inv(b*d,f)}              {e*b*d*inv(b*d,f)}')
    
    print(f'x = {sum_bnx} mod {N}')
    print(f'x = {sum_bnx%N} mod {N}')
  
def inv(n,m,show_working=True):
    #print('------------------')
    #print(f'{n}x = 1 mod {m}')
    n%=m
    #print(f'{n}x = 1 mod {m}')
    
    multiplier = 2
    initial = n
    while n%m != 1:
        n = initial
        n *= multiplier 
        n %= m
        multiplier += 1 
       
    #print(f'x = {multiplier-1} mod {m}')
    return multiplier-1



CRT(3,7,11,22,5,153)




CRT(3,5,1,7,6,8)
inv(40,7)
