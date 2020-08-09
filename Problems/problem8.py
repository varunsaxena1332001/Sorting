"""
Name = Varun Saxena
Program=Sort binary array in linear time
Branch=Btech 3rd year
course=cse
Section =A
Rollno.=60
University RollNo.=181500783

"""
n = list(map(int, input().split(',')))
count = 0
for i in range(0, len(n)):
    if n[i] == 0:
        count = count + 1
for i in range(0, len(n)):
    if i < count:
        n[i] = 0
    else:
        n[i] = 1
print('Sorted Binary Array :', n)
