from bisect import insort
class MyCalendarThree:

    def __init__(self):
        self.timeline = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        insort(self.timeline, (start, 1))
        insort(self.timeline, (end, -1))
        print(self.timeline)

        res, cumsum = 0, 0
        for _, x in self.timeline:
            cumsum += x
            res = max(res, cumsum)
        return res


obj = MyCalendarThree()
book_1 = obj.book(10, 20)
book_2 = obj.book(50, 60)
book_3 = obj.book(10, 40)
book_4 = obj.book(5, 15)
book_5 = obj.book(5, 10)
book_6 = obj.book(25, 55)
print(book_1)
print(book_2)
print(book_3)
print(book_4)
print(book_5)
print(book_6)
    