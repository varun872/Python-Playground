a=8
b=9
print(sum((a,b))) #Built-in Function

def avg(a,b):
    average=(a+b)/2
    print(average)
avg(4,6)
#print(avg(4,6)) will give None as it has no return type

def avg1(x,y):
    #gives the avg of 2 numbers
    average1=(x+y)/2
    return average1
print(avg1(5,9))
print(avg1(5,9).__doc__) #to access the comments inside a function

