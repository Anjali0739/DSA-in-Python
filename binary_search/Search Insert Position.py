# Question: https://leetcode.com/problems/search-insert-position/description/

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        ans = len(nums)
        while low<=high:
            mid = (low+high)//2
            if nums[mid] == target:
                return mid
            elif nums[mid]>target:
                high=mid-1
                if high<0:
                    return 0
            else:
                ans=mid
                low = mid+1
        return ans+1
    