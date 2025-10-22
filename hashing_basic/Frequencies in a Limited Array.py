# Question: https://www.geeksforgeeks.org/problems/frequency-of-array-elements-1587115620/0

class Solution:
    def frequencyCount(self, arr):
        #  code here
        freq = {}
        for i in range(len(arr)):
            if arr[i] in freq:
                freq[arr[i]]+=1
            else:
                freq[arr[i]]=1
                
        result = []
        for i in range(len(arr)):
            result.append(freq.get(i+1, 0))
        
        return result

