# Question: https://leetcode.com/problems/palindrome-number/description/

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        num = x
        new_num = 0
        while num>0:
            digit = num%10
            new_num = new_num*10 + digit
            num = num//10
        if x==new_num:
            return True
        return False

