import random
lst=['s','w','g']

chance=10
NoOfChance=0
ComputerPoint=0
HumanPoint=0

print("\t\t\tSNAKE\tWATER\tGUN")
print("Select:\ns --> Snake\nw --> Water\ng --> Gun")

while NoOfChance<chance:
    inpt=input("Enter your Choice: ").lower()
    rndm=random.choice(lst)

    if inpt==rndm:
        print("--------------------------------------------------\n\t\tTie\n\t0 Point to Each Player\n--------------------------------------------------\n")

    elif inpt=='s' and rndm=='g':
        ComputerPoint=ComputerPoint+1
        print(f"Your guess is {inpt} and computer guess is {rndm}\n")
        print("Computer wins 1 Point\n")
        print(f"Compuer point is {ComputerPoint} and your point is {HumanPoint}")
    
    elif inpt=='s' and rndm=='w':
        HumanPoint=HumanPoint+1
        print(f"Your guess is {inpt} and computer guess is {rndm}\n")
        print("Human wins 1 Point\n")
        print(f"Compuer point is {ComputerPoint} and your point is {HumanPoint}")
    
    elif inpt=='w' and rndm=='s':
        ComputerPoint=ComputerPoint+1
        print(f"Your guess is {inpt} and computer guess is {rndm}\n")
        print("Computer wins 1 Point\n")
        print(f"Compuer point is {ComputerPoint} and your point is {HumanPoint}")
    
    elif inpt=='w' and rndm=='g':
        HumanPoint=HumanPoint+1
        print(f"Your guess is {inpt} and computer guess is {rndm}\n")
        print("Human wins 1 Point\n")
        print(f"Compuer point is {ComputerPoint} and your point is {HumanPoint}")

    elif inpt=='g' and rndm=='w':
        ComputerPoint=ComputerPoint+1
        print(f"Your guess is {inpt} and computer guess is {rndm}\n")
        print("Computer wins 1 Point\n")
        print(f"Compuer point is {ComputerPoint} and your point is {HumanPoint}")
    
    elif inpt=='g' and rndm=='s':
        HumanPoint=HumanPoint+1
        print(f"Your guess is {inpt} and computer guess is {rndm}\n")
        print("Human wins 1 Point\n")
        print(f"Compuer point is {ComputerPoint} and your point is {HumanPoint}")
    else:
        print("--------------------------------------------------\nYou have Entered wrong input\n--------------------------------------------------\n")
        continue

    NoOfChance=NoOfChance+1
    print(f"{chance-NoOfChance} is left out of {chance}")
print("--------------------------------------------------\n\t\tGame Over!!!\n--------------------------------------------------\n")
if ComputerPoint==HumanPoint:
    print("--------------------------------------------------\n\t\tTie\n--------------------------------------------------\n")
elif ComputerPoint>HumanPoint:
    print("--------------------------------------------------\n\t\tCompuer Won\n--------------------------------------------------\n")
else:
    print("--------------------------------------------------\n\t\tYou Won\n--------------------------------------------------\n")
print(f"Your point is {HumanPoint} and computer point is {ComputerPoint}")
