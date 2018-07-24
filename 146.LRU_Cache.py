class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.table = {}
        self.capacity = capacity
        self.stack = []
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.table:
            self.updateStack(key)
            return self.table[key]
        else:
            return -1
        
    def updateStack(self, key):
        if key in self.stack:
            self.stack.remove(key)
        else:
            if len(self.stack) >= self.capacity:
                lru = self.stack.pop(0)
                self.table.pop(lru, None)
        
        self.stack.append(key)
        
    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        self.updateStack(key)
        self.table[key] = value
