class DoubleElementListIterator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0
    def __next__(self):
        if self.i < len(self.lst):
            self.i += 2
            try:
                return self.lst[self.i - 2], self.lst[self.i - 1]
            except IndexError:
                return self.lst[self.i - 2], None
        else:
            raise StopIteration()


class MyList(list):
    def __iter__(self):
        return DoubleElementListIterator(self)


for x in MyList([1,2,3,4,5]):
    print(type(x))
    print(x)
    # print(type(x))
