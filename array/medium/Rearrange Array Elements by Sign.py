# Question: https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        pos, neg = 0, 1
        result = [0]*n
        for i in range(n):
            if nums[i]>0:
                result[pos] = nums[i]
                pos+=2
            elif nums[i]<0:
                result[neg] = nums[i]
                neg+=2
        return result
    
