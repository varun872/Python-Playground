# Snake Water Gun
import random
lst=['s','w','g']
t=10
c_score=0
p_score=0
while(t):
    rand=random.choice(lst)
    choice=input("Enter s for snake\nEnter w for water\nEnter g for gun\n")
    if choice=='s':
        if rand=='w':
            print("User wins this round!")
            p_score+=1
            print(f"Scores are as follows:\nComputer:{c_score}\nUser:{p_score}\n")
        elif rand=='g':
            print("Computer wins this round!")
            c_score+=1
            print(f"Scores are as follows:\nComputer:{c_score}\nUser:{p_score}\n")
        else:
            print("Its a tie!")
            print(f"Scores are as follows:\nComputer:{c_score}\nUser:{p_score}\n")
    elif choice=='w':
        if rand=='s':
            print("Computer wins this round!")
            c_score+=1
            print(f"Scores are as follows:\nComputer:{c_score}\nUser:{p_score}\n")
        elif rand=='w':
            print("Its a tie!")
            print(f"Scores are as follows:\nComputer:{c_score}\nUser:{p_score}\n")
        else:
            print("User wins this round!")
            p_score+=1
            print(f"Scores are as follows:\nComputer:{c_score}\nUser:{p_score}\n")
    elif choice=='g':
        if rand=='w':
            print("Computer wins this round!")
            c_score+=1
            print(f"Scores are as follows:\nComputer:{c_score}\nUser:{p_score}\n")
        elif choice=='s':
            print("User wins this round!")
            p_score+=1
            print(f"Scores are as follows:\nComputer:{c_score}\nUser:{p_score}\n")
        else:
            print("Its a tie!")
            print(f"Scores are as follows:\nComputer:{c_score}\nUser:{p_score}\n")
    else:
        print("You entered wrong input")
        break
    t-=1
if c_score>p_score:
    print("The final winner after 10 rounds is Computer")
elif c_score==p_score:
    print("Its a tie after 10 rounds")
else:
    print("The final winner after 10 rounds is User")
