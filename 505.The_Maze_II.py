# BFS
# O(M*N*max(M,N))


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        m, n = len(maze), len(maze[0])
        queue = []

        def bounce(start, moves):
            nxt = []
            for d in dirs:
                r = start[0]+d[0]
                c = start[1]+d[1]
                if 0 <= r < m and 0 <= c < n and maze[r][c] == 0:
                    nxt.append(((r, c), d, moves+1))
            return nxt

        queue.extend(bounce(start, 0))

        visited = {}
        while queue:
            pos, direct, moves = queue.pop(0)

            if visited.get((pos, direct), False):
                continue
            r = pos[0] + direct[0]
            c = pos[1] + direct[1]

            if r < 0 or r >= m or c < 0 or c >= n or maze[r][c] == 1:  # wall
                if list(pos) == destination:
                    return moves
                queue.extend(bounce(pos, moves))
            else:
                queue.append(((r, c), direct, moves+1))
            visited[(pos, direct)] = True
        return -1
