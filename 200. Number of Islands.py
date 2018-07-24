class Solution:
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid or not grid[0]:
            return 0
        m,n = len(grid), len(grid[0])
        cnt = 0
        def markIsland(i,j):
            queue = [(i,j)]
            while queue:
                r,c = queue.pop(0)
                if 0<=r<m and 0<=c<n and grid[r][c] == '1':
                    grid[r][c] = 'X' # mark it
                    queue.extend([(r-1,c),(r+1,c),(r,c-1),(r,c+1)])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    cnt += 1
                    markIsland(i,j)
        return cnt
