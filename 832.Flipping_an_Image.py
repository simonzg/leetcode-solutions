class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        if not A or not A[0]:
            return A
        m,n = len(A), len(A[0])
        
        for row in range(m):
            A[row][:] = A[row][::-1]
        
        for row in range(m):
            for col in range(n):
                A[row][col] = 1-A[row][col]
        
        return A
