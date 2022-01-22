def HCF(a,b):
    if a > b:
        bigger = a
        smaller = b 
    else:
        bigger = b
        smaller = a
    
    for factor in range(1,smaller-1): #the hcf won't be bigger than the smaller number
        if a % factor == 0 and b % factor == 0:
            hcf = factor
    
    return hcf

print(HCF(198,360))
