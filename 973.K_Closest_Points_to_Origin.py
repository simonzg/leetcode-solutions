# Divide and Conquer
class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        def dist(i): return points[i][0]**2 + points[i][1]**2

        def sort(i, j, K):
            # partially sort P[i:j+1] so the first K elemnts are the smallest K elemnts
            if i >= j:
                return
            h = random.randint(i, j)
            points[i], points[h] = points[h], points[i]

            mid = partition(i, j)

            if mid-i+1 > K:
                sort(i, mid-1, K)
            elif mid-i+1 < K:
                sort(mid+1, j, K-(mid-i+1))

        def partition(i, j):
            l = i+1
            r = j
            pivot = dist(i)
            while True:
                while l < r and dist(l) < pivot:
                    l += 1
                while l <= r and dist(r) >= pivot:
                    r -= 1
                if l >= r:
                    break
                points[l], points[r] = points[r], points[l]

            points[i], points[r] = points[r], points[i]

            return r
        sort(0, len(points)-1, K)
        return points[:K]
