# Question: https://www.geeksforgeeks.org/problems/reverse-sub-array5620/1

#User function Template for python3
class Solution:
	def reverseSubArray(self,arr,l,r):
		# code here
		l-=1
		r-=1
		def helper(arr, l, r):
    		if l>=r:
    		    return
    		arr[l], arr[r]=arr[r], arr[l]
    		helper(arr, l+1, r-1)
    	
    	helper(arr, l, r)
    	return arr