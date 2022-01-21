from math import sqrt

def standardDeviation(values):

    mean = sum(values) / len(values)

    #Get square of the difference between the value and mean for all values
    diffSquared = 0
    for i in range(len(values)):
        diffSquared += (values[i] - mean) **2


    return sqrt(diffSquared / (len(values)-1))

from math import sqrt

#Like standard deviation but without the square root
def Variance(values):

    mean = sum(values) / len(values)

    #Get square of the difference between the value and mean for all values
    diffSquared = 0
    for i in range(len(values)):
        diffSquared += (values[i] - mean) **2


    return diffSquared / (len(values)-1)



if __name__ == "__main__":
    sample1 = [124,124,265,346]
    sample2 = [85,56,36,56,87,98,98,70,100,45,98,78,68,58,78]
    print(standardDeviation(sample1))
    print(standardDeviation(sample2))
    print(Variance(sample1))
    print(Variance(sample2))

