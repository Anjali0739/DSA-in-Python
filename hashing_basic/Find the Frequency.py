# Question: https://www.geeksforgeeks.org/problems/find-the-frequency/1

"""
You're given an array (arr)
Return the frequency of element x in the given array
"""
class Solution:
    def findFrequency(self, arr, x):
        # code here
        dict = {}
        for i in range(len(arr)):
            if arr[i] in dict:
                dict[arr[i]]+=1
            else:
                dict[arr[i]]=1
        return dict.get(x, 0)
    