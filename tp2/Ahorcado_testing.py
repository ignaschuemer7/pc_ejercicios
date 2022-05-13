from palabras_ES import words
import random


def computer_hangman(words_list:list=[],compute_letter:str="",triesremaning:int=5,findword:str="",letterused:str="",orden:int=0,showword:str="",listshowword:list=[],end:str="")->str:
    #el filtrado sera apor el tamaño,y luego por la probabilidad de que la letra sea la correspondiente
    listshowword.clear()
    words_list.clear()
    
    asertados=False
   

    def sizeword(findword:str)->list:
          size_findword=len(findword)
          #tamaño de la palabra a buscar
          for value in words:
              #creamos una lista a partir del tamaño de la palabra ingresada.
              if size_findword == len(value):
                  words_list.append(value)
              else:
                      continue
          return words_list   
      
    def probabilities(lista:list=[],probabilities_list:list=[],ocurrence:int=0,letters:str=0)->list:
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
     
    def yes_or_no()->str:
        while True:
            try:
               end="y"
               if end!="n" and end!="y":
                   raise ValueError
               break
            except ValueError:
                print("Oops!  This instance only takes letters beetween y (yes) or n (no).  Try again...")
        return end
    
    while True:
           findword=random.choice(words)
           if findword not in words or len(findword)!=7:
               continue
           else:
               break
            
            
    words_list = sizeword(findword)

    
    while triesremaning>0:
        
        if len(words_list)==1:
            asertados=True
            return asertados
            
        newlist=[]
    
        letterused+=compute_letter
        
        compute_letter=(probabilities(words_list))[0][1]
        
    
        
        while compute_letter in letterused:
            orden+=1
            compute_letter=(probabilities(words_list))[orden][1]
        orden=0 
        
        if triesremaning>1 or compute_letter in findword:
            question = "y"
            
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
                
                
                if final_desicion==findword:
                    asertados=True
                    return asertados
            triesremaning-=1

    return asertados
        
def play(Play:bool):
    asiertos=0
    errados=0
    while Play:
            print("In this section the compute hangman is going to test")
            for i in range(100):
                if computer_hangman()==True:
                    asiertos+=1
                else:
                    errados+=1
            print("las palabras acertadas son: ",asiertos,"y las erradas son: ",errados)
            break
def wordlist(words:tuple)->str:
    palabras=(str(words)).replace("(","").replace(")","").replace("'","")
    return "\n\n----LIST OF WORDS----\n\n" + palabras

def main():
    
    jugar=True
    while jugar:
        print("\n\nLet's play hangman! \nWhat do you want to do?\n1. Testing \n2. See words list \n3. Quit\n")
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


