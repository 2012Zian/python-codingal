word =  input("enter a word: ")
character = input("enter the character")

i = 0
count = 0

while i<len(word):
    if word[i] == character:
        count = count+1
    i=i+1

print("the number of repeats",count)