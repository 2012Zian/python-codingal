def match_words(words):
    count = 0
    list1 = []
    for i in words:
        if len(i) >1 and i[0]==i[-1]:
            count = count+1
            list1.append(i)
    print("words the start with same character and end with same character is",list1)
    return count
result = match_words(['abc','ctc','xyz','aba','1221'])
print(result)