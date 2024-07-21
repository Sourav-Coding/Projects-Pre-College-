import random
words=["Paper","Rock","Scissors"]
print("WELCOME TO ROCK PAPER & SCISSORS GAME")
while True:
    comp=random.choice(words)
    ch=int(input("1:- Rock \n2:- Paper \n3:-Scissors \n4:- Exit \nEnter Your Choice :-"))
    if (ch==1):
        user="Rock"
        print("User =",user)
        print("Computer =",comp)
        if (comp=="RocK"):
            print("*****DRAW*****...*****Nobody Wins*****")
        elif(comp=="Paper"):
            print("*****Paper Wins*****...*****Computer Wins*****")
        elif(comp=="Scissors"):
            print("*****Rock Wins*****...*****User Wins*****")
    elif (ch==2):
        user="Paper"
        print("User =",user)
        print("Computer =",comp)
        if (comp=="Paper"):
            print("*****DRAW*****...*****Nobody Wins*****")
        elif(comp=="Rock"):
            print("*****Paper Wins*****...*****User Wins*****")
        elif(comp=="Scissors"):
            print("*****Scissors Wins*****...*****Computer Wins*****")
    elif (ch==3):
        user="Scissors"
        print("User =",user)
        print("Computer =",comp)
        if (comp=="Scissors"):
            print("*****DRAW*****...*****Nobody Wins*****")
        elif(comp=="Paper"):
            print("*****Scissors Wins*****...*****User Wins*****")
        elif(comp=="Rock"):
            print("*****Rock Wins*****...*****Computer Wins*****")
    elif (ch==4):
        print("****THANK YOU FOR PLAYING****")
        break

