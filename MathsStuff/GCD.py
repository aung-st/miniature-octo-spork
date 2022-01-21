def GCD(a,b):
    if a <0:
       a = -a
    if b < 0:
        b = -b
    return (a*b) / LCM(a,b) #A well-known formula for gcd

def LCM(a,b):
    if a > b:
        greatest = a
    else:
        greatest = b

    notFound = True
    
    #Find the first number that divides both a and b evenly.
    while notFound:
        if((greatest % a ==0) and (greatest % b ==0)):
            notFound = False
            lowestCommonMultiple = greatest
            
        greatest +=1
    
    return lowestCommonMultiple

if __name__ == "__main__":
    print(LCM(15,70))
    print(GCD(15,70))
    print(GCD(-15,-70))
    print(GCD(70,15))