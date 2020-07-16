class CountSort:
    def __init__(self, a):
        c = [0 for i in range(0, max(a) + 1)]
        for i in range(0, len(a)):
            c[a[i]] = c[a[i]] + 1
        ar = []
        for i in range(0, len(c)):
            key = c[i]
            for j in range(0, key):
                ar.append(i)
        print(ar)


# d = [0, 1, 3, 3, 1, 3]
# CountSort(d)
