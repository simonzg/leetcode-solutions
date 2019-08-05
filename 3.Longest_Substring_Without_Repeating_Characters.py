# sliding window
# time complexity: O(N)
# space complexity: O(N)


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        memo = {}
        start = 0
        for i, ch in enumerate(s):
            if ch in memo:
                ans = max(ans, i-start)
                end = memo[ch]+1
                # notice the removal here, otherwise, string like "abba" won't work
                for removeCh in s[start:end]:
                    del(memo[removeCh])
                start = end
            memo[ch] = i
        ans = max(ans, len(s)-start)
        return ans
