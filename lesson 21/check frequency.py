dictionary = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}

print('original dictionary',dictionary)
k=2
count=0
for key in dictionary:
    if dictionary[key] == k:
        count = count+1


print("the frequency of value 2 is",count)