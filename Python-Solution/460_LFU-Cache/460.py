from collections import defaultdict
from collections import OrderedDict

class Node():
	def __init__(self, key, val, count):
		self.key = key
		self.val = val
		self.count = count

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.key2node = {}
        self.count2node = defaultdict(OrderedDict)
        self.minCount = None

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        # 缓存中没有这个key
        if key not in self.key2node:
        	return -1

        # 获取这个key对应的node，更新key对应的count：
        # 删掉当前count中key对应的数据
        node = self.key2node[key]
        del self.count2node[node.count][key]

        # clean memory
        if not self.count2node[node.count]:
        	del self.count2node[node.count]

		# get操作后count加1
        node.count += 1
        self.count2node[node.count][key] = node

        # 若key本来对应minCount，那get之后minCount也需要更新
        if not self.count2node[self.minCount]:
        	self.minCount += 1

        return node.val


        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if self.capacity == 0:
        	return 
        	
        # key已经在缓存中了，就相当于get（使用）一次，同时更新val
        if key in self.key2node:
        	self.key2node[key].val = value
        	self.get(key)
        	return

        # 如果key不在缓存中，且缓存已满，则删掉最近最少使用的
        if len(self.key2node) == self.capacity:
        	k, v = self.count2node[self.minCount].popitem(last = False)
        	del self.key2node[k]  

        # 添加新node
        self.count2node[1][key] = self.key2node[key] = Node(key, value, 1)      
        self.minCount = 1
        return



# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


cache = LRUCache( 2 );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       # 返回 1
cache.put(3, 3);    # 去除 key 2
cache.get(2);       # 返回 -1 (未找到key 2)
cache.get(3);       # 返回 3
cache.put(4, 4);    # 去除 key 1
cache.get(1);       # 返回 -1 (未找到 key 1)
cache.get(3);       # 返回 3
cache.get(4);       # 返回 4