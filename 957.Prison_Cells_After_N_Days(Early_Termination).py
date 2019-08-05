# Loop with early termination


class Solution:
    def prisonAfterNDays(self, cells: List[int], N: int) -> List[int]:
        days = [cells]
        n = 0
        for day in range(N):
            nxt = [0]*len(cells)
            for i in range(1, len(cells)-1):
                nxt[i] = int(cells[i-1] == cells[i+1])
            cells = nxt

            if cells in days:
                days.append(cells)
                n = days.index(cells)
                break
            else:
                days.append(cells)

        if len(days) != N+1:
            m = day-n+1
            r = (N-n) % m
            return days[r+n]
        else:
            return days[-1]
