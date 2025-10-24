# Question: https://leetcode.com/problems/rotate-array/description/

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # method 1:

        # r=k%(len(nums))
        # for _ in range(0, r):
        #     e=nums.pop()
        #     nums.insert(0, e)


        # method 2:
        # n=len(nums)
        # k=k%n
        # nums[:]=nums[n-k:]+nums[:n-k]



        # method 3:
        n=len(nums)
        k=k%n


        def reverse(nums, start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1



        reverse(nums, n-k, n-1)
        reverse(nums, 0, n-k-1)
        nums.reverse()
        
        