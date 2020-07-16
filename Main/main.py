from SortingMethods.BubbleSort import BubbleSort
from SortingMethods.CountSort import CountSort
from SortingMethods.InsertionSort import InsertionSort
from SortingMethods.SelectionSort import SelectionSort

n = int(input("enter a number 0 or 1:"))
'''
0 for BubbleSort
1 for InsertionSort
2 for SelectionSort
3 for CountSort
'''
arr = list(map(int, input("enter a array :").split(' ')))
if n == 0:
    BubbleSort(arr)
elif n == 1:
    InsertionSort(arr)
elif n == 2:
    SelectionSort(arr)
elif n == 3:
    CountSort(arr)
