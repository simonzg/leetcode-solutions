'''
REF: https://leetcode.com/problems/the-skyline-problem/discuss/61261/10-line-Python-solution-104-ms
'''
from heapq import *
class Solution:
    def getSkyline(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        
        events = sorted([(L,-H,R) for (L,R,H) in buildings] + [(R,0,None) for (_,R,H) in buildings])
        hp = [(0, float("inf"))]
        res = []
        for x,negHeight,r in events:
            while x >= hp[0][1]:
                heappop(hp)
            if negHeight:
                heappush(hp, (negHeight, r))
            if not res or res[-1][1] + hp[0][0]:
                res.append((x, -hp[0][0]))
        return res
            