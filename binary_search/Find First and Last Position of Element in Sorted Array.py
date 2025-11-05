# Question: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        first,last=-1,-1

        
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                first = mid
                high = mid - 1  
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                last = mid
                low = mid + 1  
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return [first, last]