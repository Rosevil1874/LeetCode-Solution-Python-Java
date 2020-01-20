class Solution:
    def groupAnagrams(self, strs) :
        d = {}
        for word in strs:
            key = ''.join(sorted(word))
            d[key] = d.get(key, []) + [word]
        return list(d.values())

       
        
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
s = Solution()
res =  s.groupAnagrams(strs)
print(res)
