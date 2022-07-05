def getdate():
    import datetime
    return datetime.datetime.now()
d=getdate()

def log():
    names=int(input("1)Harry\n2)Rohan\n3)Hammad\n"))
    if names==1:
        choose=int(input("1)Diet\n2)Exercise\n"))
        if choose==1:
            f=open("food1.txt","a")
            inp=input("Enter what you ate: ")
            f.write(str([d])+" "+inp+"\n")
            f.close()
        elif choose==2:
            f=open("exer1.txt","a")
            inp=input("Enter what exercise you did: ")
            f.write(str([d])+" "+inp+"\n")
            f.close()
        else:
            print("Wrong entry!!")

    elif names==2:
        choose=int(input("1)Diet\n2)Exercise\n"))
        if choose==1:
            f=open("food2.txt","a")
            inp=input("Enter what you ate: ")
            f.write(str([d])+" "+inp+"\n")
            f.close()
        elif choose==2:
            f=open("exer2.txt","a")
            inp=input("Enter what exercise you did: ")
            f.write(str([d])+" "+inp+"\n")
            f.close()
        else:
            print("Wrong entry!!")

    elif names==3:
        choose=int(input("1)Diet\n2)Exercise\n"))
        if choose==1:
            f=open("food3.txt","a")
            inp=input("Enter what you ate: ")
            f.write(str([d])+" "+inp+"\n")
            f.close()
        elif choosee==2:
            f=open("exer3.txt","a")
            inp=input("Enter what exercise you did: ")
            f.write(str([d])+" "+inp+"\n")
            f.close()
        else:
            print("Wrong entry!!")
    else:
        print("Sorry wrong input!!")

def retrieve():
    names=int(input("1)Harry\n2)Rohan\n3)Hammad\n"))
    if names==1:
        choose=int(input("1)Diet\n2)Exercise\n"))
        if choose==1:
            f=open("food1.txt")
            contents=f.read()
            print(contents)
            f.close()
        elif choose==2:
            f=open("exer1.txt")
            contents=f.read()
            print(contents)
            f.close()
        else:
            print("Wrong entry!!")

    elif names==2:
        choose=int(input("1)Diet\n2)Exercise\n"))
        if choose==1:
            f=open("food2.txt")
            contents=f.read()
            print(contents)
            f.close()
        elif choose==2:
            f=open("exer2.txt")
            contents=f.read()
            print(contents)
            f.close()
        else:
            print("Wrong entry!!")

    elif names==3:
        choose=int(input("1)Diet\n2)Exercise\n"))
        if choose==1:
            f=open("food3.txt")
            contents=f.read()
            print(contents)
            f.close()
        elif choose==2:
            f=open("exer3.txt")
            contents=f.read()
            print(contents)
            f.close()
        else:
            print("Wrong entry!!")

    else:
        print("Sorry invalid input")


while(True):
    print("You want to log or retrieve?")
    choice=int(input("1)Log\n2)Retrieve\n"))
    if choice==1:
        log()
        print("Do you wish to enter again?")
        cond=int(input("1)Yes\n2)No\n"))
        if cond==1:
            continue
        else:
            break
    elif choice==2:
        retrieve()
        print("Do you wish to enter again?")
        cond=int(input("1)Yes\n2)No\n"))
        if cond==1:
            continue
        else:
            break
    else:
        print("Wrong choice entered!!")
        print("Do you wish to enter again?")
        cond=int(input("1)Yes\n2)No\n"))
        if cond==1:
            continue
        else:
            break
