from palabras_ES import words
import random

def human_hangman(secretword="", triesremaning=5,showword=""):
    secretword=random.choice(words)
    listshowword=[]
    letterused=""
    for i in range(len(secretword)):
        listshowword.append("_")
    
    while triesremaning>0:
        
        showword=str(listshowword).replace("[","").replace("]","").replace("'","").replace(",","")
        print("\n",showword,"\t(",letterused,")")
        
        if not("_") in showword:
            return "\nCongratulations!, you find the secret word " + secretword
        
        print("\n",triesremaning,"tries remaning.")
        
        while True:
            try:
               humaninput=(input("Put a caracter or a word: ")).lower()
               if not humaninput.isalpha():
                   raise ValueError
               break
            except ValueError:
                print("Oops!  There was a problem.  Try again...")
        
        if len(humaninput)>1:
            if humaninput==secretword:
                return "\nCongratulations!, you find the secret word " + secretword
            else:
                break
            

        if humaninput not in letterused:
            letterused+=humaninput
        else: 
            
            triesremaning+=1
        if humaninput in secretword:
            for position in range(len(secretword)):
                if secretword[position] == humaninput:
                    listshowword[position]=humaninput      
    
        else:
            triesremaning-=1

    return "\nYou loose, the secret word was " + secretword

def computer_hangman(words_list=[],compute_letter="",triesremaning=5,findword="",letterused="",orden=0,showword="",listshowword=[],end=""):
    #el filtrado sera apor el tamaño,y luego por la probabilidad de que la letra sea la correspondiente
    listshowword.clear()
    words_list.clear()
    
    while True:
        try:
           findword=(input("\nPut a word and the computer will try to find :")).lower()
           if findword not in words:
               raise ValueError
           break
        except ValueError:
            print("Oops!  The word that you select, doesn't exist in the list of posible words.  Try again...")


    def sizeword(findword):
          size_findword=len(findword)
          #tamaño de la palabra a buscar
          for value in words:
              #creamos una lista a partir del tamaño de la palabra ingresada.
              if size_findword == len(value):
                  words_list.append(value)
              else:
                      continue
          return words_list   
      
    def probabilities(lista=[],probabilities_list=[],ocurrence=0,letters=0):
         probabilities_list.clear()
         for i in range(97,123):
             for word in lista:
                 #contamos la ocurrencia de cada letra en la lista completa para armar un promedio
                 if chr(i) in word:
                     ocurrence += word.count(chr(i))
                 #aprovechamos el for para contar la cantidad de letras actual en toda la lista
                 
                 if i == 97:
                     #usamos la primer letra para contar la cantidad de letras
                     letters+=len(word) 
                     
             ocurrence = ocurrence/letters
             probabilities_list.extend([(ocurrence,chr(i))])
             ocurrence=0
             
         probabilities_list.sort(reverse=True)
         
         return probabilities_list  
     
    def yes_or_no():
        while True:
            try:
               end=input("[y/n]: ").lower()
               if end!="n" and end!="y":
                   raise ValueError
               break
            except ValueError:
                print("Oops!  This instance only takes letters beetween y (yes) or n (no).  Try again...")
        return end
        
    words_list = sizeword(findword)
    
    for i in range(len(findword)):
        listshowword.append("_")
    
    while triesremaning>0:
        
        if len(words_list)==1:
            print("Is the word" ,words_list[0],"?")
            end=yes_or_no()
        if end=="n":
            return "Asume tu derrota, la palabra que elegiste si era " + words_list[0]
        elif end=="y":
            return "La computadora ha acertado, la palabra que elegiste era " + words_list[0]     
            
        newlist=[]
    
        letterused+=compute_letter
        
        showword=str(listshowword).replace("[","").replace("]","").replace("'","").replace(",","")
        print("\n",showword,"\t(",letterused,")")
        
        print("\n",triesremaning,"tries remaning.\n")
        
        compute_letter=(probabilities(words_list))[0][1]
        
        while compute_letter in letterused:
            orden+=1
            compute_letter=(probabilities(words_list))[orden][1]
        orden=0 
        while True:
            
            print("Is the letter",compute_letter,"present in the word?")
            question = yes_or_no()
            if question=="y" or question=="n":
                break
        
        for i in range(len(listshowword)):
            if findword[i]==compute_letter and question=="y":
                listshowword[i]=compute_letter
            else:
                continue
     
        if compute_letter in findword and question=="y":
             
            for word in words_list:
                for letter in range(len(findword)):
                    
                    if word[letter]==compute_letter==findword[letter]:
                        continue
                    
                    elif word[letter]!=compute_letter and compute_letter!=findword[letter]:
                        continue
                    
                    else:
                        break
                if letter==len(findword)-1 and  findword.count(compute_letter) == word.count(compute_letter):
                    newlist.append(word)
            words_list=newlist.copy()  
            
        else:
            if triesremaning == 1 and len(words_list) > 1:
                final_desicion = random.choice(words_list)
                print("Is the word" ,final_desicion,"?")
                end=yes_or_no()
                
                if end=="y" and final_desicion==findword:
                    return "La computadora ha acertado, la palabra que elegiste era " + final_desicion
            triesremaning-=1
        
    for i in range(len(letterused)-1):
        if letterused[i] in findword and letterused[i] not in showword:
            return "\nADVERTENCIA\n  Respondele adecuadamente a la maquina para que responda de manera acorde, no la engañes"

    return "Ganaste, la computadora no ha acertado la palabra seleccionada " + findword 
        
def play(Play):
    
    while Play:
        print("\nHow do you want to play?\n1. Human hangman \n2. Computer hangman \n3. Go back\n")
        while True:
            try:
               choose_mode=int(input("Select at most one option > "))
               if choose_mode !=1 and choose_mode !=2 and choose_mode !=3 :
                   raise ValueError
               break
            except ValueError:
                print("Oops!  This instance doesn´t take letters or numbers beetween 1,2 or 3.  Try again...")
        if choose_mode==1:
            print("\n----------------------------\nHUMAN HANGMAN")
            print(human_hangman())
        elif choose_mode==2:
            print("\n----------------------------\nCOMPUTER HANGMAN\n")
            print(computer_hangman())
        else:
            Play=False
        
       
def wordlist(palabras):
    palabras=(str(words)).replace("(","").replace(")","").replace("'","")
    return "\n\n----LIST OF WORDS----\n\n" + palabras

def main():
    
    jugar=True
    while jugar:
        print("\n\nLet's play hangman! \nWhat do you want to do?\n1. Play \n2. See words list \n3. Quit\n")
        while True:
            try:
               principal_menu=int(input("Select at most one option > "))
               if principal_menu !=1 and principal_menu !=2 and principal_menu !=3 :
                   raise ValueError
               break
            except ValueError:
                print("Oops!  This instance doesn´t take letters or numbers beetween 1,2 or 3.  Try again...")
        if principal_menu==1:
            print("\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            play(True)
        elif principal_menu==2:
            print(wordlist(words))
        else: 
            jugar=False
    
if __name__=='__main__':
    main()

