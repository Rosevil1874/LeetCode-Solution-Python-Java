class MyCalendarTwo:

    def __init__(self):
        self.overlaps = []
        self.calendar = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        for s, e in self.overlaps:
            if start < e and end > s:
                return False
        for s, e in self.calendar:
            if start < e and end > s:
                self.overlaps.append(( max(start, s), min(end, e) ))
        self.calendar.append((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
obj = MyCalendarTwo()
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
    