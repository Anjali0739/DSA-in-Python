
# Question: https://leetcode.com/problems/reverse-integer/


class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2**31 - 1  
        INT_MIN = -2**31 

        negative = False
        n=x
        if(x<0):
            negative = True
            n=0-x
        result=0
        while n>0:
            digit = n%10
            if result > INT_MAX // 10 or (result == INT_MAX // 10 and digit > INT_MAX % 10):
                return 0
            result = result*10 + digit
            n = n//10
        if negative:
            return 0-result
        return result
        
