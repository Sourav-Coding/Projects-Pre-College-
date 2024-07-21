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
        if (comp==user):
            print("********************\n     DRAW\n********************\n\n********************\n     Nobody Wins\n********************")
        elif(comp=="Paper"):
            print("********************\n     Paper Wins\n********************\n\n********************\n     Computer Wins\n********************")
        elif(comp=="Scissors"):
            print("********************\n     Rock Wins\n********************\n\n********************\n     User Wins\n********************")
    elif (ch==2):
        user="Paper"
        print("User =",user)
        print("Computer =",comp)
        if (comp==user):
            print("********************\n     DRAW\n********************\n\n********************\n     Nobody Wins\n********************")
        elif(comp=="Rock"):
            print("********************\n     Paper Wins\n********************\n\n********************\n     User Wins\n********************")
        elif(comp=="Scissors"):
            print("********************\n     Scissors Wins\n********************\n\n********************\n     Computer Wins\n********************")
    elif (ch==3):
        user="Scissors"
        print("User =",user)
        print("Computer =",comp)
        if (comp=="Scissors"):
            print("********************\n     DRAW\n********************\n\n********************\n     Nobody Wins\n********************")
        elif(comp=="Paper"):
            print("********************\n     Scissors Wins\n********************\n\n********************\n     User Wins\n********************")
        elif(comp=="Rock"):
            print("********************\n     Rock Wins\n********************\n\n********************\n     Computer Wins\n********************")
    elif (ch==4):
        print("********************\nTHANK YOU FOR PLAYING\n********************\n\n")
        break
