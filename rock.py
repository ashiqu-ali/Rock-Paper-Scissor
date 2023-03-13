import random
def iswin(user,opponent):
    if(user=='r'and opponent=='s') or (user=='s'and opponent=='p') or (user=='p'and opponent=='r'):
        return True
    else:
        return False

while(1):
    computer=random.choice(['r','s','p'])
    user=input("Choose Rock(r) or Paper(p) or Scissor(s) :")
    user=user.lower()

    if user==computer:
        print("It is a tie")
    elif iswin(user,computer):
        print("You Won")
    else:
        print("You Lose")