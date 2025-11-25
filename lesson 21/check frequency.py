dictionary = {'google' : 4, 'is' : 3, 'best' : 2, 'for' : 3, 'searching' : 3}

print('original dictionary',dictionary)
k=3
count=0
for key in dictionary:
    if dictionary[key] == k:
        count = count+1


print("the frequency of value 2 is",count)