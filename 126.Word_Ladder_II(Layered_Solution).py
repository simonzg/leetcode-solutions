import collections

# Reference: https://leetcode.com/problems/word-ladder-ii/discuss/40482/Python-simple-BFS-layer-by-layer


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:

        ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
        wordSet = set(wordList+[beginWord])
        if endWord not in wordSet:
            return []

        layer = collections.defaultdict(list)
        layer[beginWord] = [[beginWord]]

        leftover = wordSet
        while layer:
            newLayer = collections.defaultdict(list)
            for w in layer:
                candidates = []
                for i in range(len(w)):
                    for ch in ALPHABET:
                        newWord = w[:i]+ch+w[i+1:]
                        if newWord != w and newWord in leftover:
                            candidates.append(newWord)

                for c in candidates:
                    newLayer[c] += [l+[c] for l in layer[w]]

            if endWord in newLayer:
                return newLayer[endWord]
            layer = newLayer
            leftover -= set(newLayer.keys())
        return []
