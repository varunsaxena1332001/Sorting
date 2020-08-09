"""
Name = Varun Saxena
Program=a Triplet having maximum product in an array
Branch=Btech 3rd year
course=cse
Section =A
Rollno.=60
University RollNo.=181500783

"""
n = list(map(int, input().split(' ')))
n.sort()
a1 = max(n)
newArray = []
for i in range(0, len(n) - 1):
    for j in range(i + 1, len(n) - 1):
        mul = n[i] * n[j]
        newArray.append(mul)
newArray.sort()
MaxProduct = max(newArray) * a1
print("Maximum Product :", MaxProduct)
