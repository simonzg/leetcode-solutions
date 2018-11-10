class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        res = []
        while matrix and matrix[0]:
            res.extend(matrix[0])
            matrix = matrix[1:]
            if not matrix or not matrix[0]:
                break
            m,n = len(matrix), len(matrix[0])
            
            # transpose
            transposed = []
            for j in range(n):
                transposed.insert(0, [matrix[i][j] for i in range(m)])
            matrix = transposed
        return res
                    
        