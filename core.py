import random
var=["Rock","Paper","Scissor"]

def gam(com1,com2):
    if com1=="Rock" and com2=="Paper":
        return print("Paper Won the Match!!!")
    elif com1=="Rock" and com2=="Rock":
        return print("Match is Draw!!!")
    elif com1=="Rock" and com2=="Scissor":
        return print("Rock Won the Match!!!")
    elif com1=="Paper" and com2=="Rock":
        return print("Paper Won the Match!!!")
    elif com1=="Paper" and com2=="Paper":
        return print("Match is Draw!!!")
    elif com1=="Paper" and com2=="Scissor":
        return print("Scissor Won the Match!!!")
    elif com1=="Scissor" and com2=="Rock":
        return print("Rock Won the Match!!!")
    elif com1=="Scissor" and com2=="Paper":
        return print("Scissor Won the Match!!!")
    elif com1=="Scissor" and com2=="Scissor":
        return print("Match is Draw!!!")
    else:
        print("Values Currently not Define!!!!:")

while(str(input("Want to play Game: "))=="yes" or "Yes" or"YES"):
    print("Choose one out of any three 1. Rock 2. Paper 3. Scissor")
    com1=random.choice(var)
    player=str(input("Enter What you choose: "))
    print("Player Choose: ", player)
    print("Computer Choose: ", com1)
    gam(str(com1),str(player))


