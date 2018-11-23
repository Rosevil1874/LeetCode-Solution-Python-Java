import collections
class Solution:
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        waiting = collections.defaultdict(list)
        for word in words:
            waiting[word[0]].append(iter(word[1:]))
        for c in S:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)
        return len(waiting[None])

# S = "abcde"
# words = ["a", "bb", "acd", "ace"]
S = "dsahjpjauf"
words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
sol = Solution()
res = sol.numMatchingSubseq(S, words)
print(res)
    