l=10 #global variable:-its value won't change
def function(n):
    l=5 #local variable:- variables inside a function if called outside a function will return global variable value
    m=8
    print(l,m) #prints 5,8
    print("I have printed",n)
function("lol")
print(l) #prints 10
print(m) #won't print 8 because m is local to the function
