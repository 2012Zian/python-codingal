amounts = int(input("please enter the amount"))

note1=amounts // 100
note2=(amounts %100)//50
note3=((amounts %100)%50)//10

print("find values of hundereds",note1)
print("find values of fiftys",note2)
print("find values of tens",note3)