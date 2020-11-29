class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.res = []
        self.tmp = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.res:
            self.res.append(val)
            self.tmp[val] = len(self.res) - 1
            return True

        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.res:
            return False

        idx = self.tmp.pop(val)
        self.res[idx] = self.res[-1]
        self.res.pop()
        if idx != len(self.res):
            self.tmp[self.res[idx]] = idx

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        n = len(self.res)
        idx = random.randint(0, n - 1)
        return self.res[idx]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()