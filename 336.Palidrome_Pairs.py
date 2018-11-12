class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        res = []
        dic = dict([(w[::-1], i)for i,w in enumerate(words)])
        for i in range(len(words)):
            w = words[i]
            for j in range(len(w)+1):
                prefix, suffix = w[:j], w[j:]
                if prefix in dic and dic[prefix]!=i and suffix == suffix[::-1]:
                    res.append([i,dic[prefix]])
                if j>0 and suffix in dic and dic[suffix]!=i and prefix == prefix[::-1]:
                    res.append([dic[suffix], i])
        return res
