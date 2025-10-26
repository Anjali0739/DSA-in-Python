# Question: https://leetcode.com/problems/missing-number/description/


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        summ = n*(n+1)/2
        nums_sum = sum(nums)
        return int(summ - nums_sum)
    
