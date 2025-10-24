# Question: https://www.geeksforgeeks.org/problems/check-if-an-array-is-sorted0701/1

class Solution:
    def isSorted(self, arr) -> bool:
        # code here
        check=arr[0]
        for i in range(1, len(arr)):
            if arr[i]>=check:
                check=arr[i]
            else:
                return False
        return True
    
    