from collections import deque
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        # 统计单词中缺少某一个字母形式的单词。
        # 如： {h_t: hit, hot}
        def construct_dict(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + '_' + word[i + 1:]
                    d[s] = d.get(s, []) + [word]
            return d
        
        
        # BFS进行单词变换
        def bfs_words(begin, end, dict_words):
            queue = deque([(begin, 1)])       # 每个单词在第几步访问过
            visited = set()                 # 保存刚问过的单词
            while queue:
                word, step = queue.popleft()
                
                # 访问没访问过的单词，若已经访问过说明变换不可行
                if word not in visited:
                    visited.add(word)       # 添加访问标志
                    if word == end:         # 变换成功
                        return step
                    
                    # 将未访问过的与当前单词相差一个字母的单词加入deque，等待访问
                    for i in range(len(word)):
                        s = word[:i] + '_' + word[i + 1:]
                        neighbor_words = dict_words.get(s, [])
                        for neighbor in neighbor_words:
                            if neighbor not in visited:
                                queue.append((neighbor, step + 1))
            return 0
            
        
        d = construct_dict(wordList)
        print(d)
        return bfs_words(beginWord, endWord, d)


s = Solution()
r =  s.ladderLength("hit","cog",["hot","dot","dog","lot","log"])
print(r)