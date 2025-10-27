# Question: https://leetcode.com/problems/set-matrix-zeroes/description/

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        r=len(matrix)
        c=len(matrix[0])
        rowtrack = [0 for _ in range(r)]
        coltrack = [0 for _ in range(c)]
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    rowtrack[i]=-1
                    coltrack[j]=-1
        for i in range(r):
            for j in range(c):
                if rowtrack[i]==-1 or coltrack[j]==-1:
                    matrix[i][j]=0
                
