print("right angled triangle olf stars: ")

n = int(input("enter a number of rows"))

for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()