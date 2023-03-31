class MyTuple:
    def __init__(self, *args):
        self.data = args

    def __le__(self, other):
        if len(self.data) < len(other.data):
            return True
        elif len(self.data) > len(other.data):
            return False
        else:
            for i in range(len(self.data)):
                if self.data[i] > other.data[i]:
                    return False
                elif self.data[i] < other.data[i]:
                    return True
            return True


t1 = MyTuple(1, 2, 3)
t2 = MyTuple(1, 2, 3, 4)
t3 = MyTuple(1, 2, 4)

print(t1 <= t2)  # True
print(t2 <= t1)  # False
print(t1 <= t3)  # True
print(t3 <= t1)  # False
