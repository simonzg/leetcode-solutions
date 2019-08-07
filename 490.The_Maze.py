# key: memorize the all the stop points
# time complexity: O(M*N)
# space complexity: O(M*N)
import collections


class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """

        queue = collections.deque([])
        m, n, = len(maze), len(maze[0])

        def isWall(pos):
            i, j = pos
            if 0 <= i < m and 0 <= j < n:
                return maze[i][j] == 1
            return True

        def bounce(pos):
            i, j = pos
            return list(filter(lambda item: not isWall(item[0]), [[(i-1, j), (-1, 0)], [(i+1, j), (1, 0)], [(i, j-1), (0, -1)], [(i, j+1), (0, 1)]]))

        def move(p, d): return (p[0]+d[0], p[1]+d[1])
        visited = {}

        queue.extend(bounce(start))
        while queue:
            pos, direct = queue.popleft()
            nxt = move(pos, direct)
            while not isWall(nxt):
                pos = nxt
                nxt = move(nxt, direct)

            if tuple(destination) == pos:
                return True
            if visited.get(pos, False):
                continue
            visited[pos] = True
            queue.extend(bounce(pos))
        return False
