# Question: https://www.geeksforgeeks.org/problems/selection-sort/1

class Solution: 
    def selectionSort(self, arr):
        #code here
        n=len(arr)
        for i in range(n):
            min_ind=i
            for j in range(i+1, n):
                if arr[j]<arr[min_ind]:
                    min_ind=j
            arr[i], arr[min_ind]=arr[min_ind], arr[i]
                
        
        