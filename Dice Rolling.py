import random
n=int(input("Enter number of dice you want to throw: "))
for i in range(n):
    rand=random.randint(1,6)
    spin=random.randint(1,5)
    for i in range(spin):
        print("Dice is Rolling .....")
    print("Your Number is :",rand)
print("Thank You")

