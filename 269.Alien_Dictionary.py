class Solution:
    def alienOrder(self, words: List[str]) -> str:
        followings = {}  # key: ch, value: [] of ch that could appear after ch
        refCount = {}  # key: ch, value: #of dependent chs

        for w in words:
            for ch in w:
                followings[ch] = []
                refCount[ch] = 0

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            l1, l2 = len(w1), len(w2)
            for j in range(min(l1, l2)):
                ch1, ch2 = w1[j], w2[j]
                if ch1 != ch2:
                    if ch2 not in followings[ch1]:
                        refCount[ch2] += 1
                        followings[ch1].append(ch2)
                    break

        queue = sorted([ch for ch in refCount if refCount[ch] == 0])
        ans = ''
        while queue:
            ch = queue.pop(0)
            ans += ch
            for fch in followings[ch]:
                refCount[fch] -= 1
                if refCount[fch] == 0:
                    queue.insert(0, fch)
        return ans if sum(refCount.values()) == 0 else ""
