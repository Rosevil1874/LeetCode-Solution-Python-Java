class RLEIterator:

    def __init__(self, A):
        """
        :type A: List[int]
        """
        self.A = A
        self.idx = 0

    def next(self, n):
        """
        :type n: int
        :rtype: int
        """
        while self.idx < len(self.A) and n > self.A[self.idx]:
        	n -= self.A[self.idx]
        	self.idx += 2

        if self.idx >= len(self.A):
        	return -1

        self.A[self.idx] -= n
        return self.A[self.idx + 1]
		

# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(A)
# param_1 = obj.next(n)
        	
A = [3,8,0,9,2,5]
rle = RLEIterator(A)
print(rle.next(2))
print(rle.next(1))
print(rle.next(1))
print(rle.next(2))
    