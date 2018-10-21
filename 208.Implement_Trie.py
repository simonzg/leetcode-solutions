from collections import defaultdict
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = defaultdict()
        

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        current = self.root
        for ch in word:
            current = current.setdefault(ch, {})
        
        current['leaf'] = True
        

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        current = self.root
        for ch in word:
            if ch not in current:
                return False
            current = current[ch]
        return 'leaf' in current
        

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        current = self.root
        for ch in prefix:
            if ch not in current:
                return False
            current = current[ch]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)