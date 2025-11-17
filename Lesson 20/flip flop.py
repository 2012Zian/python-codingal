def pallindrome(t):
    e = len(t) - 1
    s=0
    while s<e:
        if t[s] != t[e]:
         return False
        s = s+1
        e=e-1
    return True
t = (1,2,3,3,2,1)
if pallindrome(t):
   print("the tuple is a flip flop")
else:
   print("the tuple is not a flip flop")
   
