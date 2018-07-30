# Reference: 
# https://leetcode.com/problems/interleaving-string/discuss/31885/Python-DP-solutions-(O(m*n)-O(n)-space)-BFS-DFS.
class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m,n,l = len(s1),len(s2),len(s3)
        if m+n!=l:
            return False
        queue, visited = [(0,0)], []
        
        while queue:
            i,j = queue.pop()
            visited.append((i,j))
            if i+j == l:
                return True
            if i<m and s1[i] == s3[i+j] and (i+1,j) not in visited:
                queue.append((i+1,j))
            if j<n and s2[j] == s3[i+j] and (i,j+1) not in visited:
                queue.append((i,j+1))
                
        return False
            
