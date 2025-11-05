# Question: https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1

class Solution:
    def countFreq(self, arr, target):
        # code here
        n = len(arr)
        first,last=0, -1

        
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                first = mid
                high = mid - 1  
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        
        low, high = 0, n - 1
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                last = mid
                low = mid + 1  
            elif arr[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return last-first+1