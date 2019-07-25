class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ''
        n = len(s)
        ans = ''

        def grow(i, j):
            l, r = i, j
            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1
            return (s[l+1:r], r-l)

        for index in range(n):
            s1, len1 = grow(index, index)
            s2, len2 = grow(index, index+1)

            res = s1 if len1 >= len2 else s2
            ans = res if len(res) > len(ans) else ans
        return ans
