# Solved by: sliding window

class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not s or not words or not words[0]:
            return []
        n = len(s)
        k = len(words[0])
        t = len(words)*k
        req = {}
        for w in words:
            req[w] = req.get(w, 0) + 1
        ans = []
        
        def findBySlideWindow(l,r, ans):
            count = {}
            while r+k<=n: # notice the =
                w = s[r:r+k]
                r += k
                if w not in req:
                    l = r
                    count.clear() # only clear in this condition
                else:
                    count[w] = count.get(w,0) + 1
                    while count[w] > req[w]:
                        count[s[l:l+k]] -= 1
                        l+=k
                    if r-l == t:
                        ans.append(l)
                
                    
        for i in range(min(k, n-t+1)): # notice the coundary
            findBySlideWindow(i,i,ans)

        return ans
