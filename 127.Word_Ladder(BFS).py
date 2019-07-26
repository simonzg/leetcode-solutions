# BFS with layer
# O(MxN)
# M: length of words
# N: total number of words
import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        wordSet = set(wordList)

        # generate memo
        memo = {}
        for w in wordSet:
            for i in range(len(w)):
                mask = w[:i]+'*'+w[i+1:]
                memo.setdefault(mask, set([])).add(w)

        if endWord not in wordSet:
            return 0

        layer = collections.defaultdict(list)
        layer[beginWord] = [[beginWord]]
        leftover = wordSet
        count = 0

        while layer:
            count += 1
            newLayer = collections.defaultdict(list)
            for w in layer:
                for i in range(len(w)):
                    mask = w[:i]+'*'+w[i+1:]
                    words = memo.get(mask, set([]))

                    if endWord in words:
                        return count+1
                    for newWord in words.intersection(leftover):
                        newLayer[newWord] += [path+[newWord]
                                              for path in layer[w]]
            leftover -= set(newLayer.keys())
            layer = newLayer
        return 0
