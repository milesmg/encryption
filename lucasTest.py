# this will check if a number n is prime, given the prime factors of n - 1
# list of prime factors of (n-1)
primeFactorList = [2,2,2,3,380038487]

# n is the number to be checked
n = 1      
for i in primeFactorList:
    n = n * i
n += 1
print ("n =" + str(n))
print()

def successive_squaring(a, b, m):
    result = 1
    base = a % m
    
    while b > 0:
        if b % 2 == 1:  # If the current bit is 1
            result = (result * base) % m
        base = (base * base) % m  # Square the base
        b = b // 2  # Shift right by 1 bit
    
    return result

# a positive integer n is prime if there exists a positive integer a, 1 < a < n, such that 
# 1) a ^ (n-1) mod n = 1
# 2) a ^ ((n-1)/q) mod n != 1 for all prime factors q of n-1
def testN (a):
    if a < n:
        if successive_squaring(a,n-1,n) == 1:
            indexer = 0
            while indexer < len(primeFactorList):
                if(a, (n-1) / primeFactorList[indexer], n) == 1:
                    return(testN (a + 1))
                indexer = indexer + 1
            return(True)
    else:
        return(False)

if testN(2):
    print(str(n) + " is prime!")
else:
    print(str(n) + " is not prime.")


