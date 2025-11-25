import array as arr

array_num  = arr.array("i",[1,2,3,4,3,6,3])
print("The original array is", str(array_num))

print("the number of accurences of 3 are", str(array_num.count(3)))
array_num.reverse()
print('reverse the orders of the array')
print(str(array_num))