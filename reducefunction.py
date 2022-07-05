from functools import reduce
list1=[1,2,3,4,5]
num=0
for i in list1:
    num+=i
print(num)

add=reduce(lambda x,y:x+y,list1)
print(add)
mult=reduce(lambda x,y:x*y,list1)
print(mult)
