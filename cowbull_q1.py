import random
name=input("enter your name")
print('...........', name ,'...........')
print("...........welcome to the cowbull",name,"...........") 
def secretum():
    number=list(range(10))
    random.shuffle (number)
    return number
# print(secretum())
def cluenum():
    num=secretum()
    list=[]
    for i in range(4):
        list.append(num[i])
    return list
# print(cluenum())
def check():
    cow=[]
    bull=[]
    num1=cluenum()
    # print(list)
    # print(num1)
# check()
    maxgue=10
    while maxgue > 0:
        guessn=int(input(" enter your guess number"))
        post=int(input("enter your position number"))
        if guessn in num1:
            index=num1.index(guessn)
            if index==post:
               if guessn not in bull:
                   bull. insert(index,guessn)
                   print("bull",bull)
               else:
                   print("you are allready use this",bull," number piz try again")
            else:
                cow.append(guessn)
                print(cow,"you can use this in diffrent position")
        if bull==num1:
            print("congratulaien you are win")
            break
        maxgue-=1
        print(maxgue,"you tern is lift")
    else:
        print("you are out","lose the guess")
        return bull
check()

def play_again():
    while True:
        again=input("you want to play agin so plz yes==y or no==n")
        if again=="y":
            check()
        else:
            break
play_again()
