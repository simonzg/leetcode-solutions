# use dictionary to record the index of list
# time complexity: O(1)


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.pos = {}
        self.vals = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.pos:
            self.vals.append(val)
            self.pos[val] = len(self.vals)-1
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.pos:
            idx = self.pos[val]
            lastVal = self.vals[-1]
            self.pos[lastVal] = idx
            self.vals[idx] = lastVal
            self.vals.pop()
            del(self.pos[val])
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        idx = random.randint(0, len(self.vals)-1)
        return self.vals[idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
