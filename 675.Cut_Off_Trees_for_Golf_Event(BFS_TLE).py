class Solution:
    def cutOffTree(self, forest: List[List[int]]) -> int:
        m, n = len(forest), len(forest[0])
        trees = []

        for i in range(m):
            for j in range(n):
                if forest[i][j] > 0:
                    trees.append((forest[i][j], i, j))
        trees = sorted(trees, key=lambda item: item[0])

        sr, sc = 0, 0
        steps = 0

        while trees:
            _, tr, tc = trees.pop(0)
            d = self.dist(forest, sr, sc, tr, tc)
            if d < 0:
                return -1
            steps += d
            sr, sc = tr, tc
        return steps

    def dist(self, forest, sr, sc, tr, tc):
        m, n = len(forest), len(forest[0])
        queue = [(sr, sc, 0)]
        visited = {}
        while queue:
            r, c, d = queue.pop(0)
            visited[(r, c)] = True
            if r == tr and c == tc:
                return d
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < m and 0 <= nc < n and forest[nr][nc] > 0 and (nr, nc) not in visited:
                    queue.append((nr, nc, d+1))
        return -1
