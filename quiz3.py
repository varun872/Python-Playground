n=18
guesses=9
while True:
    num=int(input("Enter your number: "))
    if num<18 and guesses>0:
        print("Entered number is less than n")
        guesses-=1
        print("Number of guesses left is: ",guesses)
        continue
    elif num>18 and guesses>0:
        print("Entered number is greater than n")
        guesses-=1
        print("Number of guesses left is: ",guesses)
        continue
    elif num==18 and guesses>0:
        print("You have guessed the number correctly")
        print("You guessed the number in",9-guesses,"guesses")
        break
    else:
        print("Your guesses are finished and you failed to guess the number")
        break
