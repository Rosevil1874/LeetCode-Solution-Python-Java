from collections import deque
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        len_deck = len(deck)
        q = deque( [i for i in range( len_deck )] )
        index = []
        for i in range(len_deck):
            index.append( q.popleft() )
            if len(q):
                q.append( q.popleft() )

        res = [0] * len_deck
        deck = sorted(deck)
        for i in range( len_deck ):
            res[index[i]] = deck[i]
        return res
        	
        
deck = [17,13,11,2,3,5,7]
s = Solution()
r = s.deckRevealedIncreasing(deck)
print(r)
    