import time       
import random
#librerias empleadas para lograr ciertas funciones 
def tennis():
    """
    Esta funcion, tiene contenido todo el desarrollo del script,
    que consiste en recrear un game de tenis, mediante dos modos diferentes: Automatico o manual.
    
    El script se basa principalmente en un ciclo while, 
    que dependiendo de los valores que adoptan las variables en score1 y score2,
    este se ejecuta si y solo si ninguno de los jugadores no hayan logrado ganar el game.
    
    A lo largo del script se presentan comentarios que describen que se evalua en ese punto.
    """
    print("** Welcome to the Super Tennis Annotator app **\n")
    print("How do you want to use it?\n")
    x=int(input("1. Manual input \n""2. Simulation \n""\n select gamemode: "))
    y=0
    while x!=1 and x!=2:
    #evita que se ingrese un numero no deseado en la seleccion del modo de juego.
        print("-----------------------------\n Your selection isn't valid, please put 1 or 2 \n")
        x=int(input("1. Manual input \n""2. Simulation \n""\n select gamemode: "))
    print("\n**Super tenis anotation**\n")
    player1,player2=input("Insert player 1's name: "),input ("Insert player 2's name: ")
   
    while player1==player2:
    #evita que se asignen dos nombres iguales para los jugadores.
        print("-----------------------------\n The names of players must be differents, please put differents names \n")
        player1,player2=input("Insert player 1's name: "),input ("Insert player 2's name: ")   
    score1,score2=0,0
    players=(player1,player2)
    if x==2:
        y=int(input("1. Instant result \n""2. Live match \n""\n select gamemode: "))
        while y!=1 and y!=2:
        #evita que se ingrese un numero no deseado en la seleccion del modo simulacion.
            print("-----------------------------\n Your selection isn't valid, please put 1 or 2 \n")
            y=int(input("1. Instant result \n""2. Live match \n""\n select gamemode: "))
    if y!=1:
    #si se escoge el modo resultado instaneo, no se muestra en pantalla el puntaje inicial,
    #directamente se muestra quien gano el game. 
        print("\n",player1," "*(8-len(player1)),score1)
        print("",player2," "*(8-len(player2)),score2)
        time.sleep(1.5)
    while (  (score1<=4 and score2<=4) and not(score1==4 and score2<3)and not(score2==4 and score1<3) 
           ) or  (  (0<=(score1-score2)<=1 and score1>2) or (0<=(score2-score1)<=1 and score2>2)  ):
    #Nos permite evaluar los puntajes de cada uno de los jugadores, si uno supera los 40 puntos,
    #y el otro tiene menos de 40, el while sale. 
    #Si estan en deuce, se evalua en los proximos puntos si se sale de esa condicion y uno gana, 
    #o si se mantiene el deuce en el tiempo, lo que implica que el while se va a seguir ejecutando.
           scores={0:0,1:15,2:30,3:40,4:"ad"}
           #0 es 0 , 1 es 15, 2 es 30, 3 es 40, 4 es ad
           if x==1:
           #ejecucion del modo manual
               winpoint=input("who scored? ")
               if winpoint==player1:
                   score1+=1 
               elif winpoint==player2:
                   score2+=1
           if x==2:
           #ejecucion del modo simulacion 
              winpoint=random.choice(players)
              if y==2:
              #ejecucion del modo simulacion en vivo
                 print("\n Who scored?:",winpoint,"\n")
              if winpoint==player1:
                 score1+=1  
              elif winpoint==player2:
                 score2+=1           
           if score1<=3 and score2<=3 and (y==0 or y==2):
           #se utiliza para mostrar los resultados por consola, siempre que no se hayan superado los 40 puntos.
               print("\n",player1," "*(8-len(player1)),scores[score1])
               print("",player2," "*(8-len(player2)),scores[score2])
               if y==2:
               #se emplea un delay si seleccionamos el modo de simulacion y partido en vivo.
               #Para poder visualizar el marcador.
                   time.sleep(1.4)
           else:
            #se utiliza para mostrar los resultados por consola, una vez superados los 40 puntos.
               if score1>score2 and (score1-score2)==1 and (y==0 or y==2):
               #se ejecuta si el player1 se encuentra en ventaja 
                   print("\n",player1," "*(8-len(player1)),scores[4])
                   print("",player2," "*(8-len(player2)),scores[3])
                   if y==2:
                       time.sleep(1.4)
               elif score1<score2 and (score2-score1)==1 and (y==0 or y==2):
               #se ejecuta si el player2 se encuentra en ventaja 
                   print("\n",player1," "*(8-len(player1)),scores[3])
                   print("",player2," "*(8-len(player2)),scores[4])
                   if y==2:
                       time.sleep(1.4)
               elif score1==score2 and (y==0 or y==2):
               #se ejecuta si el player1 y player2 se encuentran en deuce (empate en 40 puntos).
                   print("\n",player1," "*(8-len(player1)),scores[3])
                   print("",player2," "*(8-len(player2)),scores[3])
                   if y==2:
                       time.sleep(1.4)
    if score1<score2:
    #se determina que jugador gano, una vez que el while sale de la condicion.
           print("----------------------------\n",player2,"Wins the game" )
    else:
           print("----------------------------\n",player1,"Wins the game" )
tennis()   

 

  
    
         
     
       
