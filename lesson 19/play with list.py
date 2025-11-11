L = [5,7,5,4,3,5,4,6,5,4]
print('orginal list',L)
sum = 0
for i in L:
    sum += i
average = sum/len(L)
print("sum=",sum)
print("average",average)

L.sort()
print("the smallest element is",L[0])
print("the largest element is",L[-1])
