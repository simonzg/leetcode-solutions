# Greedy solution
# O(N)


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        memo = {}

        # build memo here
        for i, ch in enumerate(S):
            memo.setdefault(ch, []).append(i)

        start, end = 0, 0
        ans = []

        # loop through the string, and cut off the far-reaching word
        for i, ch in enumerate(S):
            end = max(memo[ch][-1], end)
            if end == i:
                ans.append(end-start+1)
                start = end+1
        return ans
