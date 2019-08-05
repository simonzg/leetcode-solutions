# Greedy solution
# time complexity: O(N)
# space complexity: O(N)


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        memo = {}  # key: character, value: last index of this char
        for i, ch in enumerate(S):
            memo[ch] = i

        start = i = 0
        end = 0
        ans = []
        while i < len(S):
            ch = S[i]
            end = max(end, memo[ch])
            if end == i:
                ans.append(end-start+1)
                start = end+1
            i += 1
        return ans
