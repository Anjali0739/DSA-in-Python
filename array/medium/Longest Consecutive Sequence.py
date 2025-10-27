# Question: https://leetcode.com/problems/longest-consecutive-sequence/description/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n = len(nums)
        my_set = set()
        for i in range(n):
            my_set.add(nums[i])
        longest = 0
        for num in my_set:
            if num-1 not in my_set:
                x=num
                count=1
                while x+1 in my_set:
                    count+=1
                    x+=1
                longest=max(longest, count)
        return longest
