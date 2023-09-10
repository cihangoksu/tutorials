''' Python program to print all primes smaller than or equal to
 n using Sieve of Eratosthenes'''
 # ref: https://www.geeksforgeeks.org/python-program-for-sieve-of-eratosthenes/
 
def SieveOfEratosthenes(n):
    prime = [True for i in range(n + 1)]
    p = 2
    while (p * p <= n):
         
        # If prime[p] is not changed, then it is a prime
        if (prime[p] == True):
             
            # Update all multiples of p
            for i in range(p ** 2, n + 1, p):
                prime[i] = False
        p += 1
    prime[0]= False
    prime[1]= False
    
    # Print all prime numbers
    prime_str = ''
    for p in range(n + 1):
        if prime[p]:
            #print (p,end=' ') #Use print(p) for python 3
            prime_str+=str(p)
    return prime_str
 

def solution(i):
    m = 20231 # empirically found number satisfying number of digits>10005
    prime_str = SieveOfEratosthenes(m)
    # print(len(prime_str))
    secretID = prime_str[i:i+5]
    print(secretID)