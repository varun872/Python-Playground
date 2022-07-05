#Dictionary is a key-value pair
d={}
print(type(d))
d1={"varun":"roti","raju":"dal","robin":{"b":"maggie","l":"chicken","d":"fish"}}
print(d1)
print(d1["robin"])
d1["ganga"]="water"
print(d1)
del d1['ganga']
print(d1)

# d2=d1
# del d2['varun']
# print(d1) #since we are equating it to d1 so deleting from d2 will affect d1 also

#shallow copy
# d2=d1.copy()
# del d1['raju']
# print(d2)

print(d1.keys())
print(d1.values())
print(d1.items())
