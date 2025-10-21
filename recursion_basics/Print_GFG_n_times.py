# Question: https://www.geeksforgeeks.org/problems/print-gfg-n-times/1

#User function Template for python3

class Solution:
    def printGfg(self, n):
        # Code here
        if n<1:
            return
        self.printGfg(n-1)
        print("GFG", end = " ")
        
        