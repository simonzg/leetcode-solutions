class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        N = len(board)

        def n2p(s):
            quot, rem = divmod(s-1, N)
            row = N - 1 - quot
            col = rem if row % 2 != N % 2 else N - 1 - rem
            return row, col

        visited = {}
        queue = [(1, 0)]

        while queue:
            n, steps = queue.pop(0)
            if visited.get(n, False):
                continue
            if n == N*N:
                return steps
            for s in range(n+1, min(N*N+1, n+7)):
                r, c = n2p(s)

                if board[r][c] != -1:
                    n2 = board[r][c]
                else:
                    n2 = s
                if not visited.get(n2, False):
                    queue.append((n2, steps+1))
            visited[n] = True
        return -1
