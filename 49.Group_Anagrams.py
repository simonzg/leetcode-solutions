class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        m = {}
        for s in strs:
            key = tuple(sorted(s))
            m[key] = m.get(key, []) + [s]
            
        return [v for k,v in m.items()]
