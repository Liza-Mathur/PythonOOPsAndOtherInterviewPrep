class IterNum():
    def __iter__(self):
        return self
    def __init__(self, n):
        self.num = n
        self.counter = 0
    def __next__(self):
        if self.counter > self.num:
            raise StopIteration
        else:
            self.counter +=1
            return self.counter-1
        
for k in IterNum(9):
    # print("I")
    print(k)

