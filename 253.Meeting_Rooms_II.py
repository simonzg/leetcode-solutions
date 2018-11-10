# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def minMeetingRooms(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        intervals.sort(key=lambda x:x.start)
        rooms = []
        for i in intervals:
            merged = False
            for m in rooms:
                if i.start >= m[-1].end:
                    m.append(i)
                    merged = True
                    break
            if not rooms or not merged:
                rooms.append([i])

        return len(rooms)
