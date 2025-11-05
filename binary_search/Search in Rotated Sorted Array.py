# Question: https://leetcode.com/problems/search-in-rotated-sorted-array/description/


# method 1
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        
        rotated_by, start = 0, 0
        for i in range(1,n):
            if nums[i-1]>nums[i]:
                start = i
                break
        else:
            start = 0
        rotated_by = start
        

        low, high = 0, n-1
        while low<=high:
            mid = (low+high)//2
            new_mid = (mid+rotated_by)%n
            if nums[new_mid] == target:
                return new_mid
            elif nums[new_mid]<target:
                low=mid+1
            else:
                high=mid-1
        return -1

            

# method 2
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            # Left half is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Right half is sorted
            else:
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1