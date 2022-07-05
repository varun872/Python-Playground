l=[["a",1],['b',2],['c',3],['d',4]]
for item in l:
    print(item)
dict1=dict(l)
for key,value in dict1.items():
    print(key,value)
    
l1=[2,'t',7,'ghost',75,4]
for i in l1:
    if type(i)==int and i>6:
        print(i)
    
