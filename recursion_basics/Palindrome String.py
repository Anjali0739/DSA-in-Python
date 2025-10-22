# Question: https://www.geeksforgeeks.org/problems/palindrome-string0817/1

class Solution:
    def isPalindrome(self, s):
        # code here
        
        # method 1:
        # l=0
        # r=len(s)-1
        # while(l<r):
        #     if s[l]!=s[r]:
        #         return False
        #     l+=1
        #     r-=1
        # return True
        
        # method 2:
        l=0
        r=len(s)-1
        def helper(s, l, r):
            if l>=r:
                return True
            if s[l]!=s[r]:
                return False
            return helper(s, l+1, r-1)
        return helper(s, l, r)
        

