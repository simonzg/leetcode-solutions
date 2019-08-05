# BFS with visited words list (avoid duplicate)
# time complexity: O(M*N)
# space complexity: O(M*N)
import collections


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # generate memo for faster access
        memo = {}
        for w in wordList+[beginWord]:
            for i in range(len(w)):
                mask = w[:i]+"*"+w[i+1:]
                memo.setdefault(mask, []).append(w)

        if endWord not in wordList:
            return 0

        wordSet = set(wordList)
        queue = collections.deque([([beginWord], 1)])
        visited = {}
        while queue:
            path, moves = queue.popleft()
            w = path[-1]
            if w == endWord:
                return moves
            if w in visited:
                continue
            for i in range(len(w)):
                mask = w[:i]+"*"+w[i+1:]
                for extendWord in memo.get(mask, []):
                    queue.append((path+[extendWord], moves+1))
            visited[w] = True
        return 0
