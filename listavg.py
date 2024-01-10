import timeit

class ListAverage:
    def __init__(self, lst):
        self.lst = lst.copy()
        self.total = 0
        for num in self.lst:
            self.total += num

    def add(self, num):
        self.lst.append(num)
        self.total += num

    def compute_avg(self):
        total = 0
        for num in self.lst:
            total += num
        return total / len(self.lst)

    def compute_avg_faster(self):
        # implement this method
        return self.total / len(self.lst)

test = ListAverage([43,5,4,23,54])

faster = timeit.timeit(stmt=f'{test.compute_avg_faster()}')
slow = timeit.timeit(stmt=f'{test.compute_avg()}')

print(f'{faster - slow}')