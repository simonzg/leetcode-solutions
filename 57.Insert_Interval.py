# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        start = newInterval.start
        end = newInterval.end
        
        r = 0
        l = 0
        while r< len(intervals):
            itv = intervals[r]
            if start <= itv.end:
                if end < itv.start:
                    break
                start = min(start, itv.start)
                end = max(end, itv.end)
                r+=1
            else:
                l+=1
                r+=1
        return intervals[:l] + [Interval(start,end)] + intervals[r:]
         
