class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        words = s.split(' ')
        reversedWords = []
        for word in words:
        	word = word[::-1]
        	reversedWords.append(word)
        return (' ').join(reversedWords)
		

s = "Let's take LeetCode contest"
r = Solution().reverseWords(s)
print(r)