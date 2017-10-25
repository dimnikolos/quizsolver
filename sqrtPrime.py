import functools
import math


class factorDict():
    """
    A wrapper for a factors dictionary where the key is the factor
    and the value is the power of the factor
    """
    def __init__(self):
        self.factors = {}
    def add(self,factor):
        if factor in self.factors:
            self.factors[factor] += 1
        else:
            self.factors[factor] = 1
    def powerString(self):
        """
        Print the result in the form of powers
        and square roots
        """
        retStrList = []
        for factor in self.factors:
            if self.factors[factor] == 0.5:
                retStrList.append("√" + str(factor))
            elif self.factors[factor] == 1:
                retStrList.append(str(factor))
            elif self.factors[factor] == 1.5:
                retStrList.append(str(factor) + "*√" + str(factor))
            elif self.factors[factor] == int(self.factors[factor]):
                retStrList.append(str(factor) + "^" + str(int(self.factors[factor])))
            else:
                retStrList.append(str(factor) + "^" + str(int(self.factors[factor]-0.5)) + "*√" + str(factor))
        return("*".join(retStrList))
    def numberString(self):
        number = 1
        retSqrtList = []
        for factor in self.factors:
            if self.factors[factor] == int(self.factors[factor]):
                number *= math.pow(factor,self.factors[factor])
            else:
                number *= math.pow(factor,self.factors[factor]-0.5)
                retSqrtList.append("√" + str(factor))
        if number == 1:
            return("*".join(retSqrtList))
        elif retSqrtList == []:
            return(str(int(number)))
        else:
            return(str(int(number)) +"*" + "*".join(retSqrtList))





def prime_sieve(limit):
    """
    Eratosthenes' sieve
    """
    prime_list = []
    for i in range(2,limit+1):
        #for any number until the limit
        #check the primes that you have so far
        for aPrime in prime_list:
            if i % aPrime == 0:
                #i is not a prime, no need
                #to check other primes from
                #list
                break
        else:
            #i is prime since there was no
            #break
            yield i
            prime_list.append(i)

def primeFact(x):
    """
    Computes and returns a factorDict class
    for a number x
    """
    factors = factorDict()#initialize dictionary
    for aPrime in prime_sieve(math.ceil(math.sqrt(x))):
        #if x is divided by aPrime
        #do the division and add a factor
        #to the factor dictionary
        while x % aPrime == 0:
            factors.add(aPrime)
            x = x//aPrime
        #proceed to next prime
    #the number that is left must be added
    #to the factors if its larger than one
    #e.g. if x is not divided by any prime
    # number until math.ceil(math.sqrt(x))
    #then x is a prime itself and should 
    #be added to the factors
    if x > 1:
        factors.add(x)
    return(factors)
            
def squareRoot(x):
    """
    Computes and returns the factors of the 
    square root as a simple dictionary
    """
    sqrtFactors = factorDict()
    for factor in primeFact(x).factors:
        sqrtFactors.factors[factor] = primeFact(x).factors[factor]/2
    return(sqrtFactors)

while True:
    x = int(input("Give number:"))
    print("x" + len(str(int(x)))*" " + " = " +str(int(x)))
    print("x" + len(str(int(x)))*" " + " = " +primeFact(x).powerString())
    print("√"+str(x)+ " = " + squareRoot(x).powerString())
    print("√"+str(x)+ " = " + squareRoot(x).numberString())