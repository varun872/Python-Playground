# def func1():
#     print("Subscribe Now")

# func2=func1
# del func1
# func2() # prints Subscribe Now because another copy of func1 has been created in func2

def smart_div(func):
    def swap(a,b):
        if(a<b):
            a,b=b,a
        return func(a,b)
    return swap

@smart_div
def div(a,b):
    print(a/b)
# div=smart_div(div)
div(3,6)


def pos_sum(func):
    def pos(*args):
        args=list(args)
        for i in range (len(args)):
            args[i]+=1
        return func(*args)
    return pos

@pos_sum
def add(*args):
    sum1=0
    args=list(args)
    for i in args:
        sum1+=i
    print(sum1)

num=[0,1,2,3,4]
add(*num)
