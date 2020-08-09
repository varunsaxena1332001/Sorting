"""
Name = Varun Saxena
Program=Inversion count of an Array
Branch=Btech 3rd year
course=cse
Section =A
Rollno.=60
University RollNo.=181500783

"""
'''
Description= If (i,j) and (A[i]>A[j]) then the pair (i,j) is an inversion of an array
'''
n = list(map(int, input().split(',')))
count = 0
for i in range(0, len(n) - 1):
    for j in range(i + 1, len(n)):
        if i < j and n[i] > n[j]:
            count = count + 1
print('Inversion count is', count)
