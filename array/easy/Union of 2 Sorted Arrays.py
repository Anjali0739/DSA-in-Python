# Question: https://www.geeksforgeeks.org/problems/union-of-two-sorted-arrays-1587115621/1

class Solution:
    def findUnion(self, a, b):
        # code here 
        i=j=k=0
        n=len(a)
        m=len(b)
        result = []
        while i<n and j<m:
            if a[i]<b[j]:
                if not result or result[-1] != a[i]:
                    result.append(a[i])
                i+=1
            elif a[i]>b[j]:
                if not result or result[-1] != b[j]:
                    result.append(b[j])
                j+=1
            else:
                if not result or result[-1] != a[i]:
                    result.append(a[i])
                i+=1
                j+=1
            k+=1
        while i<n:
            if not result or result[-1] != a[i]:
                result.append(a[i])
            i+=1
            k+=1
        while j<m:
            if not result or result[-1] != b[j]:
                result.append(b[j])
            j+=1
            k+=1
        return result

