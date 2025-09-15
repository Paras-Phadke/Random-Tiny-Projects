import math
global unprimes
rang = int(input("Enter the num: "))
unprimes =[]
primes = []
for i in range(1, rang + 1):
    for j in range(1,int( math.sqrt(i) )+ 1):
        if  i % j  == 0 and j != 1 and i not in unprimes:
            unprimes.append(i)

for i in range(1,rang + 1):
    if i not in unprimes and i!=1 :
        primes.append(i)

print(primes,len(primes))