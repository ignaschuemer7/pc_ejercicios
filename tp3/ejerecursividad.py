from operator import truediv


def palindroma(palabra:str)->bool:
    if len(palabra)==3 and palabra[0]==palabra[2] or len(palabra)==1:
        return True
    elif palabra[-1]==palabra[0]:
        return palindroma(palabra[1:-1])
    else:
        return False
    
print(palindroma("neuquen"))     
#%%
def dardos(n:int)->bool:
    if n%5==0 or n%7==0:
        return True
    else:
        return dardos(n-7) or dardos(n-5)
print(dardos(9))
#%%
def dardos():
    if n in (0,5,7):
        return True
    elif n in (1,2,3,4,6):
        return False
    else:
        return dardos(n-5) or dardos(n-7)