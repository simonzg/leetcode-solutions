# key is the counter representation of the words
# 26 0s: (0,0,0,.....0) and add 1 for each alphabet occurence
# time complexity: O(NK)
# space complexity: O(NK)


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        memo = {}
        for s in strs:
            key = [0]*26
            for ch in s:
                i = ord(ch)-ord('a')
                key[i] += 1
            key = tuple(key)
            memo.setdefault(key, []).append(s)
        return memo.values()
