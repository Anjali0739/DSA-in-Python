# Question: https://www.geeksforgeeks.org/problems/prime-number2314/1
import math
class Solution:
    def isPrime(self, n):
        # code here

        
        count = 0
        
        # method 1:
        # for i in range(1, n+1):
        #     if n%i==0:
        #         count+=1
            
        # if count>2 or n<=1:
        #     return False
        # return True
        
        
        # method 2:
        for i in range(1, int(math.sqrt(n))+1):
            if n%i==0 or n%(i*i)==0:
                count+=1
        if count>=2 or n<=1:
            return False
        return True