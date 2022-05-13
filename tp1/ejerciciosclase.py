def buscar(one_list,number):
    #busqueda lineal
    for i in range(0, len(one_list)):
        if number==one_list[i]:
            return i


def print_list(one_list):
    for value in one_list:
        print(value)
def print_reverse_list(one_list):
    for i in range(len(one_list)-1,-1,-1):
        print(one_list[i])
        
def reverse_list(one_list):
    output=[]
    for i in range(len(one_list)-1,-1,-1):
        output.append(one_list[i])
    return output
def main():
    one_list=[1,2,99,4]
    output=buscar(one_list,99)
    print( output )  
        
    
if __name__=="__main__":
    main()
        
#%%
def palabra(patron,palabra):
    if len(patron)==len(palabra):
        x=0
        for i in range(0,len(patron)):
            if patron[i]=="?" or patron[i]==palabra[i]:
                x+=1  
                print(x)
        if x==i+1:
            return True
        else:
            return False
    else:
        return False
print("el resultado es",palabra("ho??aa","honkaa"))

#%%
#define a funtion that removes from a given array of integers all the values contained in a second array 
#ej input: [1,1,2,3,1,2,3,4,],[1,3] --> output [2,2,4]

def remove_all_marked(l1,l2,ls):
    for value in l1:
        if not (value in l2):
            ls.append(value)
            
    return ls           
print(remove_all_marked([1,2,3,5,2,6,5,5], [2,5],[]))
#%%
"""Write a function with the following properties:
    - takes two lists- returns a list of all possibilities to pair as many elements as possible from both lists while keeping the order of the elements
    - output format is a list of lists of tuples, or a list with an empty list, if no pairs are possible
    - inner lists can be of any order (see tests)HintsIf both input lists are of equal length, then every item of one list will be paired with an item of the other list (see first example) -> results in only one sublist. 
    If both input lists are of different length and not empty,then every item of the shorter list will be paired, 
    but not every item of the larger list -> results in more than onesublist, because there are more then one possibilities to omit items from the larger list.
    Example 1Pair elements of ['c', 'o', 'd', 'e'] with elements of ['w', 'a', 'r', 's']Expected Result:[[('c', 'w'), ('o', 'a'), ('d', 'r'), ('e', 's')]]"""

def pair_elements(l1,l2):
    result=[]
    
    for first, second in zip(l1,l2):
        result.append((first,second))
    return result

print(pair_elements(["c","d","x","y"],["w","a","f","t"]))

#hacer lo mismo pero de todos con todos
#%%
def pair_elements(l1,l2):

    result=[]
    
    for value in l1 :
        for value2 in l2:
           result.append((value,value2))    
           
    return result

print(pair_elements(["c","d","x","y"],["w","a","f","t"]))

#%%
#buscar una carta entre 40. 

def carta_faltante(maso1,maso2):
    
    
    
    for carta1,carta2 in zip (maso1,maso2):
        if carta1 != carta2:
            return carta1
        elif carta1==39:
            return 39
     

def main():
    maso1=[]
    maso2=[]
    for i in range (1,41):
        maso1.append(i)
        maso2.append(i)
    del(maso2[39])
    
    print(carta_faltante(maso1,maso2))
 
if "__name__"=="__main__":
    main()
main()


#%%
import time
def carta_faltante(maso1):
    primero=0
    ultimo=len(maso1)-1
    
    #la posicion 38 corresponde al ultimo elemento de la lista 
    
    while primero<=ultimo:
       mitad=(ultimo+primero)//2
       print("la mitad es",mitad)
       if maso1[mitad-1] == maso1[mitad]-2:
       #si falta la carta 20, el elemento 21 del elemento 19, estan consecutivos.
           return mitad+1
           
       elif maso1[mitad-1]==mitad:
           #cuando la carta es mayor a 20
           primero=mitad+1
           if maso1[ultimo]==39:
               return maso1[ultimo]+1
               
           if maso1[mitad-1] == maso1[mitad-1]-2 :
           #si la hay un salto de posicion en la lista, en elementos consecutivos, la carta se encuentra en ese valor    
               return mitad+1
       else:
           #cuando la carta es menor a 20
           ultimo=mitad-1
           
           if maso1[mitad-1] == maso1[mitad]-2:
           #si la hay un salto de posicion en la lista, en elementos consecutivos, la carta se encuentra en ese valor    
               return mitad+1
       time.sleep(1)
       if mitad==1:
           return 1
       
       
       
def main():
    maso1=[]
    cartaquefalta=23
    for i in range (1,41):
        maso1.append(i)
    print(maso1)
    del(maso1[cartaquefalta-1])
    print(maso1)
    print("la carta que falta es",carta_faltante(maso1))


main()
#%%
'''Escribir un programa que dado un día del año (1 a 366) ingresado por el usuario, imprima el día
de la semana que le corresponde. Debe asumir que el año comenzó, por ejemplo, un domingo. Por
ejemplo: si se ingresa '5', imprime 'jueves', si se ingresa '10' imprime 'martes', si se ingresa '294'
imprime 'sabado'.'''

def dia_random(dia):
    diadelasemana=dia%7
    dias=("domingo","lunes","martes","miercoles","jueves","viernes","sabado")
    diaelegido=dias[diadelasemana]
    return diaelegido
def main():
    dia=int(input("ingrese un numero entre el 1 y el 366, y se determinara que dia de la semana es en el año: "))
    while dia>366 or 0>dia:
        dia=int(input("ingrese un numero entre el 1 y el 366, y se determinara que dia de la semana es en el año: "))
    print("el dia elegido es",dia_random(dia))


main()


#%%
'''
en un juego de dardos el centro vale 7 puntos, el borde 5 y fuera 5 puntos.
Dado un puntaje final, validar si responde a un juego valido.
dardos (10) ->true 
Dardos(15) ->True
Dardos(13) ->False '''

def dardos(puntaje):
    x,y=puntaje,puntaje
    if (puntaje%7 == 0) or (puntaje%5 == 0) or (puntaje%7 == 5):
        return True
    else:
        while ((x%7 != 0 and x%7 !=5) and (x%5 != 0)) and ((y%7 != 0 and y%7 !=5) and (y%5 != 0)):
            x-=7
            y-=5
            print(x,y)
            if x<5 and y<5:
                return False
        return True
            
        
    
print("el score ingresado es",dardos(int(input("ingrese un puntaje :"))))

#%%
def buscar_A(palabra,ocurrencia=0):
    for i in palabra:
        if i=="A":
            ocurrencia+=1
    return ocurrencia

def main():
    print("la Letra A, aparece",buscar_A('AnanA'),"veces")

if '__name__'=='__main__':
    main()

#%%
def cambiarip(ip:str,nuevoip:str):
    
    for i in ip:
        if i==".":
            nuevoip+="[.]"
        else:
            nuevoip+=i
    return nuevoip

print("el nuevo ip es",cambiarip('123.134.454',""))
#%%
def cambiaripmejor(ip:str):
    
    ip = ip.replace(".","[.]")
    return ip

print("el nuevo ip es",cambiaripmejor('123.134.454'))
#%%
def cambiaripconjoin(ip):
    
    ip = ip.split(".")
    x="[.]".join(ip)
    return x

print("el nuevo ip es",cambiaripconjoin('123.134.454'))

#%%
def piedrasquesonjoyas(piedras,joyas):
    cantidadj,cantidadp=0,0
    
    for x in piedras:
        for y in joyas:
            if x==y:
                cantidadj+=1
                break
           
    return cantidadj
print("la cantidad de joyas que hay es",piedrasquesonjoyas("ggjaA", "AAAAj"))
#%%
def encripto(palabra,llave):
    x=llave
    palabraencriptada=""
    for i in palabra:
        
        if llave>=25:
            llave=llave%25
        if ord(i)+llave>=123:
            x-=25
        elif ((ord(i)+llave>=91) and not(ord(i)>96 and ord(i)<123)):
            x-=25
        
        letrasnum=ord(i)+llave
        letrasstr=chr(letrasnum)
        palabraencriptada+=letrasstr        
    return palabraencriptada
print("la palabra encriptada es",encripto("zzzz",90))
#falta los negativos

#%%
def encriptado(text,s):
    palabranueva=""
    for i in text:
        if i.isupper():
            palabranueva+=chr((ord(i)+s-65) % 26 + 65)
        elif i.islower():
            palabranueva+=chr((ord(i)+s-97) % 26 + 97)
        else:
            palabranueva+=i
    return palabranueva

print("la palabra encriptada es",encriptado("aaa",-9))




#%%
'''Escribir una función que reciba una fecha en formato AAAA-MM-DD y retorne un tupla de 3 enteros
con la fecha. En el formato AAAA-MM-DD, AAAA representa el año con 4 dígitos, MM el mes con 2 dígitos, y
DD el día con 2 dígitos'''

def fecha_a_tupla(fecha):
    x=[]
    lista=fecha.split("-")
    for i in lista:
        i=int(i)
        x.append(i)
    tuplanueva=tuple(x)
    return tuplanueva
    
print("la tupla asociada a esa fecha es: ",fecha_a_tupla("2022-12-3000"))
#%%
'''Escribir una función que reciba una lista de tuplas, donde cada tupla contiene un nombre y una fecha
(la fecha puede ser una tupla o una cadena en formato AAAA-MM-DD, a elección de quien programa la
función). La función debe retornar True si todas las personas son de sagitario. Considere el caso particular
en que la lista contenga 8 tuplas, los primeros 6 nombres sean "Gachi", "Pachi", "Lorena", "novio", "exnovio"
y "Andrea", y sean todos de sagitario, en cuyo caso debe imprimirse un mensaje acorde, además de retornar
el correspondiente True.'''

def sagitario(listadetuplas):
    x=55
    for tupla in listadetuplas:
        for value in tupla:
             if (31>=tupla[0]>=22 and tupla[1]==11) or  (0<tupla[0]<=21 and tupla[1]==12):
                 continue
             else:
                 return "no son de sagitario",x
    return "son de sagitario" ,x         
    
print("todas las personas de la lista",sagitario([(21,12,3,"igna"),(1,11,5,"agustin")]))

                
#%%
"piedra papel o tijera"
import random
def ppot(persona):
    listapalabras=("piedra","papel","tijera")
    ph,pm=0,0
    while (pm<3 and ph<3) :
       humano=input("ingrese piedra, papel, o tijera :")
       eleccionhumano=listapalabras.index(humano)
       eleccionmaquina=random.randint(0,2)
       print("\n maquina :", listapalabras[eleccionmaquina])
       if eleccionmaquina>eleccionhumano and not(eleccionmaquina==2 and eleccionhumano==0):
           pm+=1
       elif eleccionmaquina<eleccionhumano and not( eleccionhumano==2 and eleccionmaquina==0 ):
           ph+=1
       elif eleccionmaquina==2 and eleccionhumano==0:
           ph+=1
       elif eleccionhumano==2 and eleccionmaquina==0:
           pm+=1
       else:
           continue
       
       print("\nel puntaje de la maquina es: ", pm,"\nel puntaje del usuario es: ",ph)
    if pm>ph:
         return "\nla maquina ha ganado"
    else:
         return "\n" + persona + " ha vencido a la maquina"
     
print(ppot("ignacio"))  
           
#%%   
m={"hol":4,"ihds":4,33:"ret","holdg":7}
print(m)
m["camino"]=56768    
print(m)
print(m.values())
#%%
'''
En este ejercicio practicaremos el concepto de filtrado: queremos quedarnos con algunos elementos
de entre otros tantos, para ello:
Escribir una función que reciba una lista y retorne True o False dada alguna condición sobre sus
elementos. Por ejemplo, una función que recibe una lista de al menos 3 elementos y retorna True si
el segundo es mayor al tercero y la suma de estos dos es mayor 20.
Escribir una función llamada filtrar que recibe una lista L y una función f y retorne una lista con
aquellos elementos de L que al aplicarles f (al ejecutar f con cada uno de ellos como argumento,
individualmente) devuelven True.
Resolver el ejercicio anterior utilizando la función filtrar desarrollada en el inciso anterior 
'''

def filtrado(L):
    
    for i in range (len(L)):
        
        if L[i]==int(L[i]) or L[i]==float(L[i]):
            L[i]=funcion(L[i])
            
        else:
            continue
            
    return L
def funcion(y):
    y=y*3
    return y

def main():
    print(filtrado([21,5,6]))
    
main()   
#%%
def filtrado(L,f=0):
    M=[]
    print(M,L)
    for i in L:
        
       if type(i)==str:
           continue
       
       elif i==int(i) or i==float(i):
            f=funcion(i)
            if f == True:
                M.append(i)
            else:
               continue
           
    return M
        
def funcion(i):
    if i>5 and i%2==0:
        return True
    else:
        return False

def main():
    print(filtrado([22,"26","gya"]))
    
main()    
#%%
L=["fief","dwifj",'fhrf',34]
for i,x in enumerate(L):
    print("\n\n",i,"\n\n\n",x)

#%%
"""Suponga que tiene dos dados, asumiendo en ambos la misma probabilidad de ocurrencia por
cada número (1/6). El juego consiste en dos participantes que, por turno, deben tirar los dos dados
simultáneamente y seguir las siguientes reglas:
1. Si ambos dados salen con diferente número (ej: 3 y 6), se suman y se le asigna ese valor como
puntaje al jugador. Luego pasa a jugar el siguiente participante.
2. Si ambos dados salen con el mismo número (ej: 4 y 4), se suman y se le asigna ese valor como
puntaje al jugador, pero en este caso el jugador puede volver a tirar, de manera tal que el
nuevo puntaje se acumule con el anterior, concluyendo su turno al sacar los dos números
distintos (caso 1).
El jugador que haya obtenido mayor puntaje será el ganador de la mano.
1. ★☆☆ Describa el juego mediante un algoritmo.
2. ★☆☆ Realice el diagrama de flujo del algoritmo propuesto.
3. ★★★ Implemente el juego en forma interactiva, para 2 participantes.
Para simular el lanzamiento de datos, pida a cada usuario que presione una tecla cuando deba
arrojar los dados.
En base a este reglamento, implemente un algoritmo que le solicite a cada jugador que tire los dados
oprimiendo una tecla, luego genere dos números aleatorios entre 1 y 6 (simulando los dos dados)
siguiendo las reglas del juego. Al concluir el turno de cada jugador, deberá indicarse el puntaje de ese
participante y pasar al otro.
Ayuda: para generar números aleatorios de 1 a 6 puede usar la función
random.randint(1,6) importando el módulo random con import random."""
import random
def dados(dado1, dado2):
    puntaje=0
    
    if dado1==dado2: 
        while dado1==dado2:
           puntaje+=dado1+dado2
           dado1,dado2=tiro_dados()
           
    if dado1!=dado2:
        puntaje+=dado1+dado2
    return puntaje
        
        
    
def tiro_dados():
      dado1=random.randint(1,6)
      print("dado1",dado1)
      
      dado2=random.randint(1,6)
      print("dado2",dado2)
      
      return dado1,dado2


def main():
    ganador=False
    print("Juego de dados\n\nComienza el jugador 1\n")
    tiros=0
    p1=0
    p2=0
    
    while tiros<=6:
        comenzar=input("presione la tecla s, para tirar los dados :")
       
        while comenzar!="s":
            comenzar=input("presione la tecla s, para tirar los dados :")
            
        if tiros%2==0:
                print("\nturno de jugador uno")
                p1+=dados(*tiro_dados())
                print("\nel puntaje actual del player uno es",p1)

                print("\nel puntaje actual del player dos",p2)
        else:
                print("\nturno de jugador dos")
                p2+=dados(*tiro_dados())
                print("\nel puntaje actual del player uno es",p1)

                print("\nel puntaje actual del player dos",p2)
        
        
        tiros+=1
    if p1>p2:
        print("\nel ganador es el jugador 1")
    elif p1==p2:
        print("\nempate")
    else:
        print("\nel ganador es el jugador 2")

main()
  
#%%
#EXECPCIONES
def errores():
    
    try:
        x=input("ingrese un numero :")
        x=int(x)
    except ValueError:
        print("error value")
        
    '''if x>2:
         raise Exception ("rraise exceptionn") '''
errores()        
#%%

def milenials(lista):
    lista_milenials=[]
    for i in lista:
        
        fecha=i[1]
        ano=int(fecha[-4:])
        
        if ano>=1981 and ano<1996:
            lista_milenials.append(i[0])
    return lista_milenials

datos_personales=[("roberto","12/1/2002"),("ignacio","23/3/1982"),("marcelo","17/2/1989")]

lista_milenials=milenials(datos_personales)
print(lista_milenials)

#%%
lista=["marcos","udbwf",'jnec']
#lista.remove("marcos")
lista+=["chaca","wiliam"]
lista[2:3]=[1,2,3]
print(lista)

x=("===").join(lista)
#transforma listas a cadenas, las separacion de las listas esta dada por los caracteres entre parentesis.
print(x)
y=x.split("===")
#transforma cadenas a listas, las separacion de las listas esta dada por los caracteres entre parentesis.
print(y)
#for i,x in enumerate(lista):
 #   print(i,x)

#%%
from palabras_ES import words


def busqueda_binaria(lista=words, element="brangutan"):
    inicio=0
    fin=len(words)-1
    while fin>=inicio:
        medio=(inicio+fin)//2
        if ord((words[medio][0]))==ord(element[0]):
            return "La palabra ha sido encontrada en la posicion",medio
        elif ord((words[medio][0]))<=ord(element[0]):
            inicio=medio+1
        else:
            fin=medio-1
            
    return -1
print(busqueda_binaria())

#%%
l=[10,2,3,7,2,5]
l.sort(reverse=True)

print(l)
lista=["marcos","udbwf",'jnec',43]
#lista.remove("marcos")
lista+=["chaca","wiliam"]

lista.remove(43)
print(lista)
#%%
"""Escriba un programa que tome un número entero entre 0 y 100 provisto por el usuario e
imprima en la consola un mensaje indicando si el número es primo o no. Si el número no es un entero
entre 0 y 100, que imprima un mensaje indicando que el número ingresado no es entero entre 0 y
100."""

def numeros_primos(n):
    l_primos=[]
    
    for i in range(1,n+1):
        l_primos.append(i)
    
    
    x=l_primos.copy()
    
    print(x)
    for nums in l_primos:
        print(nums)
        for cada_num in range(2,nums):
            if nums % cada_num==0:
                x.remove(nums)
                break
            else:
                continue
    return x

print(numeros_primos(344))

#%%
import random
ale={2:"duhuf","sdiwhdw":23,"gaga":1234}

ale["gutavo"]=56
del(ale[2])
print(ale.values())
print(ale)
a=[23,45,87]
a+=[23]
print (a)
#%%
def busqueda_debases(secuencia,objetivo):
    x=0
    cadena=""
    if objetivo in secuencia:
        for i in range (len(secuencia)-1):
            for n in range (len(objetivo)-1):
                if secuencia[i+n]==objetivo[n]:
                    x+=1
                if x==len(objetivo):
                    cadena=secuencia[(i-3):(i+1)]+objetivo+secuencia[(i+n+1):(n+12)]
                    return cadena
    return cadena

print(busqueda_debases("hdebybhsjhdctttcacattuydubcububuch","cubuih"))

#%%
def promedio(nombres,notastps,parcial):
    r=[]
    notas=0
    for i in range(len(nombres)-1):
        for x in notastps:
            promedio=(notastps[i][x]+parcial[i])/4
            if promedio>=4:
                r.extend([nombres[i],promedio])
        return r
#%%
l=["duefb","dubwud","uh","edhied"]
for index in range(len(l)-1):
    if l[index]=="duefb":
        del(l[index])
        index-=1
    if index==len(l):
        break

print(l)
      
                    





            
