import random
comp=0
ply1=0
compcount=0
ply1count=0
L=("Rock","Scissor","Paper")
while(compcount<=5 and ply1count<=5):
    comp=random.choice(L)
    print("\n1.Rock    2.Scissor   3.Paper")
    ply1=input("Enter your choice:")
    if(comp==ply1):
        print("\nTie,No one wins this round")
        print("\nComputer chose",comp,"\nPlayer chose",ply1)
        print("Player Score=",ply1count)
        print("Computer Score=",compcount)
    elif(comp=="Rock" and ply1=="Scissor"):
        compcount+=1
        print("Computer wins this round")
        print("\nComputer chose",comp,"\nPlayer chose",ply1)
        print("Player Score=",ply1count)
        print("Computer Score=",compcount)
    elif(ply1=="Rock" and comp=="Scissor"):
         ply1count+=1
         print("\nPlayer1 wins this round")
         print("\nComputer chose",comp,"\nPlayer chose",ply1)
         print("Player Score=",ply1count)
         print("Computer Score=",compcount)

    elif(ply1=="Paper" and comp=="Rock"):
         ply1count+=1
         print("\nPlayer1 wins this round")
         print("\nComputer chose",comp,"\nPlayer chose",ply1)
         print("Player Score=",ply1count)
         print("Computer Score=",compcount)
    elif(comp=="Paper" and ply1=="Rock"):
        compcount+=1
        print("\nComputer wins this round")
        print("\nComputer chose",comp,"\nPlayer chose",ply1)
        print("Player Score=",ply1count)
        print("Computer Score=",compcount)
    elif(ply1=="Scissor" and comp=="Paper"):
        ply1count+=1
        print("\nPlayer1 wins this round")
        print("\nComputer chose",comp,"\nPlayer chose",ply1)
        print("Player Score=",ply1count)
        print("Computer Score=",compcount)
    elif(comp=="Scissor" and ply1=="Paper"):
        compcount+=1
        print("\nComputer wins this round")
        print("\nComputer chose",comp,"\nPlayer chose",ply1)
        print("Player Score=",ply1count)
        print("Computer Score=",compcount)
    if(ply1count==5):
        print("Player Score=",ply1count)
        print("Computer Score=",compcount)
        print("Player wins the game")
        break
    if(compcount==5):
        print("Player Score=",ply1count)
        print("Computer Score=",compcount)
        print("Computer wins the game")
        break
    

