class SelectionSort:
    def __init__(self, a):
        for i in range(0, len(a)):
            mini = i
            for j in range(i + 1, len(a)):
                if a[j] < a[mini]:
                    mini = j
            if mini != i:
                c = a[mini]
                a[mini] = a[i]
                a[i] = c
        print(a)

# d = [4, 3, 2, 1]
# SelectionSort(d)
