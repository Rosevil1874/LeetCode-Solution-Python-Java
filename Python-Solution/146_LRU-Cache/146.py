import collections
class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.cache = collections.deque([])  # 用来存key，记住存放顺序
        self.dict = {}                      # 用来存key-value
        

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.dict:
            return -1
        self.cache.remove(key)
        self.cache.append(key)
        return self.dict[key]


    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        # 若这个key已经在缓存中了，为了“使用”它一次，要把它拿出来重新放进去，表示最近使用
        if key in self.cache:
            self.cache.remove(key)

        # 否则：若缓存满了，将最近最少使用的元素移除，为新key腾出空间。同时要将在dict中的记录也删去。
        elif len(self.cache) == self.capacity:
            v = self.cache.popleft()
            self.dict.pop(v)
        self.cache.append(key)
        self.dict[key] = value
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

cache = LRUCache( 2 );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       # 返回  1
cache.put(3, 3);    # 该操作会使得密钥 2 作废
cache.get(2);       # 返回 -1 (未找到)
cache.put(4, 4);    # 该操作会使得密钥 1 作废
cache.get(1);       # 返回 -1 (未找到)
cache.get(3);       # 返回  3
cache.get(4);       # 返回  4