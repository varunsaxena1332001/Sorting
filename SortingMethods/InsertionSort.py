class InsertionSort:
    def __init__(self, p):
        self.a = p
        self.b = [p[0]]
        for i in range(1, len(self.a)):
            for j in range(0, len(self.b)):
                if self.a[i] < self.b[j]:
                    self.b.insert(j, self.a[i])
                    break
        print(self.b)

# d = [4, 3, 2, 1]
# InsertionSort(d)
