# Question: https://www.geeksforgeeks.org/problems/floor-in-a-sorted-array-1587115620/1

class Solution:
    def findFloor(self, arr, x):
        # code here
        low = 0
        high = len(arr)-1
        ans = -1
        while low<=high:
            mid = (low+high)//2
            if arr[mid]>x:
                high = mid -1
            elif arr[mid]<=x:
                ans = mid
                low = mid+1
            
        return ans
        
        