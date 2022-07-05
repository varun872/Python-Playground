# def printf(a,b,c,d):
#     print(a,b,c,d)

# try:
#     printf("harry","hammad","rohan","skillf","shivam")
# except Exception as e:
#     print(e)
# Will throw error because the function takes only 4 arguements as inputs but we have given 5

def printf(normal,*args):
    print(type(args))
    print(normal)
    for i in args:
        print(i)

har=['harry','barry','carrie']
printf('varun',*har)
