# Question: https://www.geeksforgeeks.org/problems/factorial5739/1

class Solution:
    # Function to calculate factorial of a number.
    def factorial(self, n: int) -> int:
        # code here
        if n==1:
            return n
            
        return n*self.factorial(n-1)
    
    