class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        def sieve_of_eratosthenes(left,right):
            ans=[]
            prime = [True for i in range(right+1)]
            p=2
            while (p*p <= right):
                if prime[p]==True:
                    for i in range(p*p,right+1,p):
                        prime[i]=False
                p+=1
            
            for p in range(left,right+1):
                if prime[p] and p>1:
                    ans.append(p)
            
            return ans

        primes=sieve_of_eratosthenes(left,right)
        ans=[-1,-1]
        diff=inf

        for i in range(1,len(primes)):
            if primes[i]-primes[i-1] < diff:
                diff=primes[i]-primes[i-1]
                ans=[primes[i-1],primes[i]]

        return ans
