# sort & merge
# time complexity: O(N*logN)
# space complexity: O(N)


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
        intervals.sort(key=lambda v: v[0])
        for interval in intervals:
            merged = False
            for i, room in enumerate(rooms):
                if room[-1][1] <= interval[0]:
                    room.append(interval)
                    rooms[i] = room
                    merged = True
                    break
            if not merged:
                rooms.append([interval])
                continue

        return len(rooms)
