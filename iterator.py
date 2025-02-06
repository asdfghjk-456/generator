class CycleIterator:
    def __init__(self, iterable):
        self.iterable = iterable
        self.index = 0
    def __iter__(self):
        return self
    def __next__(self):
        if not self.iterable:
            raise StopIteration
        value = self.iterable[self.index]
        self.index = (self.index + 1) % len(self.iterable)
        return value
it = CycleIterator([1, 2, 3])
for _ in range(7):
 print(next(it))