##--Machine learning
##--Finding the value of mean,median,mode,stander-deviation,variance from a list of number


# --import needed
import numpy

# -- Your data
x = [23, 43, 45, 65, 34, 45, 45, 67, 98, 7, 65]

# -- Mean
def mean(x):
    return numpy.mean(x)

# -- Median
def median(x):
    return numpy.median(x)

# -- Standard deviation
def Std(x):
    return numpy.std(x)

# -- Variance
def variance(x):
    return numpy.var(x)

# -- Print results using f-strings
print(f"Value of X : {x}")
print(f"Mean : {mean(x)}")
print(f"Median : {median(x)}")
print(f"Standard Deviation : {Std(x)}")
print(f"Variance : {variance(x)}")   
