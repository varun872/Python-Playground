list1=['3','4','5']
for i in range(len(list1)):
    list1[i] = int(list1[i])
print(list1)
# This can be avoided and map can be used since all elements in the list needs to be converted

numbers=list(map(int,list1)) #syntax 1st->Operation/Function to be applied, 2nd->The data(list)
# print(map(int,list1)) #returns a map object
print(numbers)

def cb(a):
    return a*a*a

list2=[1,2,3,4,5]
cube=list(map(cb,list2)) #map can use user defined functions
print(cube)

str1=['laugh','cry','break','kill']
ing=list(map(lambda x:x+'ing',str1)) #map can also use lambda functions
print(ing)
