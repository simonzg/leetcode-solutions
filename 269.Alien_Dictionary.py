# Reference: https://leetcode.com/problems/alien-dictionary/discuss/156130/Python-Solution-with-Detailed-Explanation-(91)


class Solution:
    def alienOrder(self, words: List[str]) -> str:
        edges = {}  # key: ch, val: set of ch followed key
        prereqCounts = {}  # key: ch, val: prerequisite count
        ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

        for w in words:
            for ch in w:
                prereqCounts[ch] = 0

        for i in range(len(words)-1):
            for j in range(min(len(words[i]), len(words[i+1]))):
                a, b = words[i][j], words[i+1][j]
                if a != b:
                    edges.setdefault(a, set([]))

                    if b not in edges[a]:
                        edges[a].add(b)
                        prereqCounts[b] += 1
                    break
        queue = []
        for ch in ALPHABET:
            if prereqCounts.get(ch, -1) == 0:
                queue.append(ch)

        res = []

        while queue:
            ch = queue.pop(0)
            res.append(ch)
            for t in edges.get(ch, []):
                prereqCounts[t] -= 1
                if prereqCounts[t] == 0:
                    queue.insert(0, t)

        return ''.join(res) if len(res) == len(prereqCounts) else ''
