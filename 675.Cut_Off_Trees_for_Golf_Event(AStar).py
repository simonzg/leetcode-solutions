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
        heap = [(0, 0, sr, sc)]
        cost = {(sr, sc): 0}
        while heap:
            f, g, r, c = heapq.heappop(heap)
            if r == tr and c == tc:
                return g
            for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                if 0 <= nr < m and 0 <= nc < n and forest[nr][nc]:
                    ncost = g+1+abs(nr-tr)+abs(nc-tc)
                    if ncost < cost.get((nr, nc), 9999):
                        cost[(nr, nc)] = ncost
                        heapq.heappush(heap, (ncost, g+1, nr, nc))
        return -1
