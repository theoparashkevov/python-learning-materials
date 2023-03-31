class MyTuple:
    def __init__(self, *args):
        self.data = args

    def __lt__(self, other):
        for i in range(min(len(self.data), len(other.data))):
            if self.data[i] < other.data[i]:
                return True
            elif self.data[i] > other.data[i]:
                return False
        return len(self.data) < len(other.data)


t1 = MyTuple(1, 2, 3)
t2 = MyTuple(1, 2, 3, 4)
t3 = MyTuple(1, 2, 4)

print(t1 < t2)  # True
print(t2 < t1)  # False
print(t1 < t3)  # True
print(t3 < t1)  # False
