from fractions import gcd
import math


class quadratic():
    def __init__(self,coeflist):
        self.quad = {}
        for (power,coef) in enumerate(coeflist):
            self.quad[len(coeflist)-1-power] = coef
    def __str__(self):
        return('+'.join([(str(self.quad[power])+'x^'+str(power)) 
            for power in sorted(self.quad.keys(),reverse=True)]))
    def findmn(self):
        a = self.quad[2]
        b = self.quad[1]
        c = self.quad[0]
        #find numbers m and n so that 
        #m*n = a*c and m+n = b
        for m in range(1,abs(a*c)):
            if a*c/m == a*c//m:
                n = a*c // m
                if m+n == b:
                    return(m,n)
        for m in range(-1,-abs(a*c),-1):
            if a*c/m == a*c//m:
                n = a*c // m
                if m+n == b:
                    return(m,n)
        return(None)
    def box(self):
        if not self.findmn():
            return(None)
        else:
            a = self.quad[2]
            b = self.quad[1]
            c = self.quad[0]
            (m,n) = self.findmn()
            print(m,n)
            row1Coef = math.copysign(gcd(abs(a),abs(m)),a)
            row2Coef = math.copysign(gcd(abs(n),abs(c)),n)
            col1Coef = math.copysign(gcd(abs(a),abs(n)),a)
            col2Coef = math.copysign(gcd(abs(m),abs(c)),m)
            print(str(self))
            print('('+str(row1Coef)+'x+'+str(row2Coef)+')('+str(col1Coef)+'x+'+str(col2Coef)+')')

def main():

    quadratic([2,7,5]).box()

main()
            
