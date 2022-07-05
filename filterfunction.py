list1=[1,2,3,4,5,6,7,8,9]
odd=list(filter(lambda x:x%2==1,list1))
print(odd)

f=list(filter(lambda x:x>15,map(lambda x:x+10,list1)))
print(f)
# filter works on True/False conditions

str1=['laugh','cry','break','kill']
def length_str(a):
    return len(a)>7
ing=list(filter(length_str,map(lambda x:x+'ing',str1)))
print(ing)

tup=('varun','raju','vella','harry')
def starts(a):
    return a.startswith('v')
names=list(filter(starts,tup))
print(names)
