# Question: https://www.geeksforgeeks.org/problems/number-of-factors1435/1

import math
class Solution:
    def countFactors (self, n):
        # code here
        
        count=0
        
        # method 1:
       
        # for i in range(1, n+1):
        #     if n%i==0:
        #         count += 1
        # return count
        
        # method 2:
        for i in range(1, int(math.sqrt(n))+1):
            if n%i==0:
                if i*i==n:
                    count+=1
                    continue
                count+=2
        return count
    
    