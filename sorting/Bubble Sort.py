# Question: https://www.geeksforgeeks.org/problems/bubble-sort/1

class Solution:
    def bubbleSort(self,arr):
        # code here
        n=len(arr)
        for i in range(n):
            for j in range(n-1):
                if arr[j]>arr[j+1]:
                    arr[j], arr[j+1]=arr[j+1],arr[j]
                    
                
                