# Simple BFS
# time complexity: O(M*N)
# space complexity: O(M*N)
import collections


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        def paintIsland(i, j):
            queue = collections.deque([(i, j)])
            while queue:
                r, c = queue.popleft()
                if 0 <= r < m and 0 <= c < n and grid[r][c] == '1':
                    grid[r][c] = 'x'
                    queue.extend([(r-1, c), (r+1, c), (r, c-1), (r, c+1)])

        m, n = len(grid), len(grid[0])
        count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    paintIsland(i, j)
                    count += 1
        return count
