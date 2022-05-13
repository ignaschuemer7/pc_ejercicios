from palabras_ES import words
import random

def print_console(listshowword:list,letterused:str)->tuple:
    """
    Parameters
    ----------
    listshowword : list
        It contains the secretword, but incomplete.
    letterused : str
        It contains the letters that the user or the computer risk.

    Returns
    -------
    tuple
        It contains the word with blank spaces and the letters those you use.

    """
    
    showword=str(listshowword).replace("[","").replace("]","").replace("'","").replace(",","")
    
    return  ("\n" + showword + "\t("+ letterused +")",showword)

def list_showword(word:str,listshowword:list=[])->list:
    """
    Parameters
    ----------
    word : str
        It contain the secret word.
    listshowword : list, optional
        It contains the secretword, but incomplete. The default is [].. The default is [].

    Returns
    -------
    list
        listshowword.

    """
    listshowword.clear()
    
    for i in range(len(word)):
        listshowword.append("_")
    return listshowword

def human_hangman(secretword:str="", triesremaning:int=5,showword:str="",letterused:str="")->str:
    """
    Parameters
    ----------
    secretword : str, optional
        This word is selected by the computer and the user will trie to find it. The default is "".
    triesremaning : int, optional
        It use to count the tries that the user has. The default is 5.
    showword : str, optional
        It contain the word with blank spaces that you watch at the console. The default is "".
    letterused : str, optional
        It contains the letters that the user risk. The default is "".

    Raises
    ------
    ValueError
        It use to avoid the breakup of the code by the inputs.

    Returns
    -------
    str
        The result of the game.

    """
    secretword=random.choice(words)
    listshowword=list_showword(secretword)
    
    while triesremaning>0:
        
        print(print_console(listshowword, letterused)[0])
        
        showword=print_console(listshowword, letterused)[1]
        
        if not("_") in showword:
            return "\nCongratulations!, you find the secret word " + secretword
        
        print("\n",triesremaning,"tries remaning.")
        
        while True:
            try:
               humaninput=(input("Put a caracter or a word: ")).lower()
               if not humaninput.isalpha() or len(humaninput)!=len(secretword) and len(humaninput)!=1:
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
        
            
        if humaninput in secretword:
            for position in range(len(secretword)):
                if secretword[position] == humaninput:
                    listshowword[position]=humaninput      
        else:
            triesremaning-=1

    return "\nYou loose, the secret word was " + secretword

def computer_hangman(words_list:list=[],compute_letter:str="",triesremaning:int=5,findword:str="",letterused:str="",position:int=0,showword:str="",listshowword:list=[],end:str="")->str:
    """
    Parameters
    ----------
    words_list : list, optional
        It contains a lots of words. The default is [].
    compute_letter : str, optional
        It use to save the letter that the computer risk. The default is "".
    triesremaning : int, optional
        It use to count the tries that the computer has. The default is 5.
    findword : str, optional
        Its the word that the computer trie to find. The default is "".
    letterused : str, optional
        It contains the letters that the computer risk. The default is "".
    position : int, optional
        It use to select the most probable letter that the computer. The default is 0.
    showword : str, optional
        It contain the word with blank spaces that you watch at the console. The default is "".
    listshowword : list, optional
        It contains the findword, but incomplete. The default is [].
    end : str, optional
        The string can be "y"(yes) or "n"(no). The default is "".

    Raises
    ------
    ValueError
        It use to avoid the breakup of the code by the inputs.
    Returns
    -------
    str
        The result of the game.

    """
    #el filtrado sera apor el tamaño,y luego por la probabilidad de que la letra sea la correspondiente
    listshowword.clear()
    words_list.clear()
    
    def sizeword(findword:str)->list:
          """
        Parameters
        ----------
        findword : str
            This word was put by the user, and the computer will try to find it.

        Returns
        -------
        list
            Words that have a similar lenght of the findword.

        """
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
        """
        Parameters
        ----------
        lista : list, optional
            it use to contain a list of words. The default is [].
        probabilities_list : list, optional
            It use to contain a list whith a percentage of posible letters. The default is [].
        ocurrence : int, optional
            It use to contains the ocurrence of letters. The default is 0.
        letters : str, optional
            It use to count all of the letters in lista. The default is 0.

        Returns
        -------
        list
            probabilities_list.

        """
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
        """
        Raises
        ------
        ValueError
            It use to avoid the breakup of the code by the inputs..

        Returns
        -------
        str
            The string can be "y"(yes) or "n"(no).

        """
        while True:
            try:
               end=input("[y/n]: ").lower()
               if end!="n" and end!="y":
                   raise ValueError
               break
            except ValueError:
                print("Oops!  This instance only takes letters beetween y (yes) or n (no).  Try again...")
        return end
    
    
    while True:
        try:
           findword=(input("\nPut a word and the computer will try to find :")).lower()
           if findword not in words:
               raise ValueError
           break
        except ValueError:
            print("Oops!  The word that you select, doesn't exist in the list of posible words.  Try again...")
            
    words_list = sizeword(findword)
    
    listshowword=list_showword(findword)
    
    while triesremaning>0:
        
        if len(words_list)==1:
            print("Is the word" ,words_list[0],"?")
            end=yes_or_no()
        if end=="n":
            return "Assume your defeat, the word you chose if it was" + words_list[0]
        elif end=="y":
            return "The computer guessed right, the word you chose was "+ words_list[0]     
            
        newlist=[]
    
        letterused+=compute_letter
        
        showword=print_console(listshowword, letterused)[1]
        
        compute_letter=(probabilities(words_list))[0][1]
        
        print(print_console(listshowword, letterused)[0])
        
        print("\n",triesremaning,"tries remaning.\n")
        
        while compute_letter in letterused:
            position+=1
            compute_letter=(probabilities(words_list))[position][1]
        position=0 
        
        if triesremaning>1 or compute_letter in findword:
            print("Is the letter",compute_letter,"present in the word?")
            question = yes_or_no()
            
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
                    return "The computer guessed right, the word you chose was " + final_desicion
            triesremaning-=1
        
    for i in range(len(letterused)-1):
        if letterused[i] in findword and letterused[i] not in showword:
            return "\nWARNING\n Respond appropriately to the machine so that it responds accordingly, do not deceive it"

    return "You won, the computer did not guess the selected word correctly " + findword 
        
def play(Play:bool):
    """

    Parameters
    ----------
    Play : bool
        This function contains a menu of posible games moods.

    Raises
    ------
    ValueError
        It use to avoid the breakup of the code by the inputs.

    Returns
    -------
    None.

    """
    
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
        
       
def wordlist(words:tuple)->str:
    """
    Parameters
    ----------
    words : tuple
        It use to show the list of words in the console.

    Returns
    -------
    str
        This function returns the list of words in a string.

    """
    palabras=(str(words)).replace("(","").replace(")","").replace("'","")
    return "\n\n----LIST OF WORDS----\n\n" + palabras

def main():
    """
    This is the main of the code, there are the principal menus here.

    Raises
    ------
    ValueError
        It use to avoid the breakup of the code by the inputs.

    """
    
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

