class BubbleSort:
    def __init__(self, a):
        b = a
        for i in range(len(a)):
            for j in range(len(b) - 1):
                if b[j] < b[j + 1]:
                    c = b[j + 1]
                    b[j + 1] = b[j]
                    b[j] = c
        print(b)

# arr = [1, 2, 3, 4]
# BubbleSort(arr)
