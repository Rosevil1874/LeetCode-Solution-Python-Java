class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.pos = {}
        

    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.pos:
        	self.nums.append(val)
        	self.pos[val] = len(self.nums) - 1
        	return True
        return False
        
    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.pos:
        	idx = self.pos[val]
        	last = self.nums[-1]
        	self.nums[idx] = last
        	self.pos[last] = idx
        	self.nums.pop()
        	self.pos.pop(val, 0)
        	return True
        return False

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]
       

# Your RandomizedSet object will be instantiated and called as such:
RandomizedSet randomSet = new RandomizedSet()
randomSet.insert(1);
randomSet.remove(2);
randomSet.insert(2);
randomSet.getRandom();
randomSet.remove(1);
randomSet.insert(2);
randomSet.getRandom();
