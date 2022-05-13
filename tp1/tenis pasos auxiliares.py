import time       
import random
def tennis():
    print("** Welcome to the Super Tennis Annotator app **\n")
    print("How do you want to use it?\n")
    x=int(input("1. Manual input \n""2. Simulation \n""\n select gamemode: "))
    y=0
    while x!=1 and x!=2:
        print("-----------------------------\n Your selection isn't valid, please put 1 or 2 \n")
        x=int(input("1. Manual input \n""2. Simulation \n""\n select gamemode: "))
    print("\n**Super tenis anotation**\n")
    player1,player2=input("Insert player 1's name: "),input ("Insert player 2's name: ")
    if x==2:
        y=int(input("1. Instant result \n""2. Live match \n""\n select gamemode: "))
        while y!=1 and y!=2:
            print("-----------------------------\n Your selection isn't valid, please put 1 or 2 \n")
            y=int(input("1. Instant result \n""2. Live match \n""\n select gamemode: "))
    while player1==player2:
        print("-----------------------------\n The names of players must be differents, please put differents names \n")
        player1,player2=input("Insert player 1's name: "),input ("Insert player 2's name: ")
    score1,score2=0,0
    players=(player1,player2)
    if y!=1:
        print("\n",player1," "*(8-len(player1)),score1)
        print("",player2," "*(8-len(player2)),score2)
        time.sleep(1.5)
    while (  (score1<=4 and score2<=4) and not(score1==4 and score2<3) and not(score2==4 and score1<3)  ) or  (  (0<=(score1-score2)<=1 and score1>2) or (0<=(score2-score1)<=1 and score2>2)  ):
           scores={0:0,1:15,2:30,3:40,4:"ad"}
           if x==1:
               winpoint=input("who scored? ")
               if winpoint==player1:
                   score1+=1  
               elif winpoint==player2:
                   score2+=1
           if x==2:
              winpoint=random.choice(players)
              if y==2:
                 print("\n Who scored?:",winpoint,"\n")
              if winpoint==player1:
                 score1+=1 
              elif winpoint==player2:
                 score2+=1        
           if score1<=3 and score2<=3 and (y==0 or y==2):
               print("\n",player1," "*(8-len(player1)),scores[score1])
               print("",player2," "*(8-len(player2)),scores[score2])
               if y==2:
                   time.sleep(1.4)
           else:
               if score1>score2 and (score1-score2)==1 and (y==0 or y==2):
                   print("\n",player1," "*(8-len(player1)),scores[4])
                   print("",player2," "*(8-len(player2)),scores[3])
                   if y==2:
                       time.sleep(1.4)
               elif score1<score2 and (score2-score1)==1 and (y==0 or y==2):
                   print("\n",player1," "*(8-len(player1)),scores[3])
                   print("",player2," "*(8-len(player2)),scores[4])
                   if y==2:
                       time.sleep(1.4)
               elif score1==score2 and (y==0 or y==2):
                   print("\n",player1," "*(8-len(player1)),scores[3])
                   print("",player2," "*(8-len(player2)),scores[3])
                   if y==2:
                       time.sleep(1.4)
    if score1<score2:
           print("----------------------------\n",player2,"Wins the game" )
    else:
           print("----------------------------\n",player1,"Wins the game" )
tennis()         
if __name__=="__main__":
    tennis()
print("tenis")


        