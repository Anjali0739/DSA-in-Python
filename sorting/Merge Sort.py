# Question: https://www.geeksforgeeks.org/problems/merge-sort/1

class Solution:
    def merge_arr(self,arr, l, mid, r):
        left = arr[l:mid+1]
        right = arr[mid+1:r+1]
        i, j=0, 0
        k=l
        n, m = len(left), len(right)
        while i<n and j<m:
            if left[i]<=right[j]:
                arr[k]=left[i]
                i+=1
            else:
                arr[k] = right[j]
                j+=1
            k+=1
        
        if i<n:
            while i<n:
                arr[k] = left[i]
                i+=1
                k+=1
        
        if j<m:
            while j<m:
                arr[k] = right[j]
                j+=1
                k+=1

    
    
    def mergeSort(self, arr, l, r):
        #code here
        if l>=r:
            return
            
        mid = (l+r)//2
        self.mergeSort(arr, l, mid)
        self.mergeSort(arr, mid+1, r)
        
        self.merge_arr(arr, l, mid, r)
        
        



