import random
bank=int(input("Enter your Bank Balance :-"))
print("THE GAME IS STARTING....")
res=0
while (bank>0):
    while True:
        bet=int(input("Enter the Amount you want to bet :- "))
        remain=bank-bet
        print("Your Remaining Balance is ",remain)
        confm=int(input("ARE YOU SURE?\nPress 1 = Yess\nPress 2 = No\n----->"))
        if (confm==1):
            break
    print("Enter your preferred choice to gamble")
    print("1  2  3  4  5\n6  7  8  9  10\n11  12  13  14  15\n16  17  18  19  20\n21  22  23  24  25\n26  27  28  29  30\nAny EVEN\nAny Odd\nDivisible By 7")
    print("(1)  Guess the exact number = x100")
    print("(2)  Any Even = x10")
    print("(3)  Any Odd = x10")
    print("(4)  Divisible By 7 = x50")
    print("WRONG GUESS = x0")
    ch=int(input("Enter Your Choice :-"))
    rand=random.randint(1,30)
    if (ch==1):
        ch1=int(input("Enter the Exact Number:-"))
        if (ch1==rand):
            bet_w=bet*100
            res=res+bet_w
            print("****CONGRATULATION YOU HAVE HIT THE JACKPOT****")
            print("Your bet was :- ",bet)
            print("Your winning :- ",bet_w)
        else:
            bet_w=bet*0
            print("Sorry You Have Guessed The Wrong Number")
            print("Your bet was :- ",bet)
            print("****You Lost The Whole Bet****")
    if (ch==2):
        if(rand%2==0):
            bet_E=bet*10
            res=res+bet_E
            print("****CONGRATULATION****")
            print("Your bet was :- ",bet)
            print("Your winning :- ",bet_E)
        else:
            bet_E=bet*0
            print("Sorry You Have Guessed The Wrong Number")
            print("Your bet was :- ",bet)
            print("****You Lost The Whole Bet****")
    if (ch==3):
        if(rand%2!=0):
            bet_O=bet*10
            res=res+bet_O
            print("****CONGRATULATION****")
            print("Your bet was :- ",bet)
            print("Your winning :- ",bet_O)
        else:
            bet_O=bet*0
            print("Sorry You Have Guessed The Wrong Number")
            print("Your bet was :- ",bet)
            print("****You Lost The Whole Bet****")
    if (ch==4):
        if(rand%7==0):
            bet_S=bet*10
            res=res+bet_S
            print("****CONGRATULATION****")
            print("Your bet was :- ",bet)
            print("Your winning :- ",bet_S)
        else:
            bet_S=bet*0
            print("Sorry You Have Guessed The Wrong Number")
            print("Your bet was :- ",bet)
            print("****You Lost The Whole Bet****")
    bank=bank-bet
    con=int(input("(1) Double or (2) Backout?\n----->"))
    if(con==2):
        print("Your bet was",bet)
        print("You Won ",res)
        remain=remain+res
        print("Your Bank Balance is ",remain)
        break
    
    
    


            

         
    
    

             
