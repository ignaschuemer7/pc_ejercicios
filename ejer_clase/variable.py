def main():
    a=1380*(5/2)
    print("a gasto",a)
    b=410
    print("b gasto",b)
    c=800
    print("c gasto",c)
    d=0
    print("d gasto",d)
    e=0
    print("e gasto",e)
    total=a+b+c+d+e
    promedio =(total/5)
    print("el total gastado es",total)
    print("a tiene que pagar ",promedio-a)
    print("b tiene que pagar",b)
#%%
def tennis(player1,player2):
    print("hola")

tennis("grthr","gerg")

#%%
n=100000

for i in range(1,n):
    
   if i % 11 == 0 and i % 12 == 0:
       print(i)
       break
   else:
       n=+1

#%%
def main(anosdelpadre,anosdelhijo):
    edadelpadre = (anosdelpadre-anosdelhijo)*2 
    return abs(anosdelpadre-edadelpadre)
main(34,19)
#%%
def areaperimeter(altura,ancho):
   
    if altura==ancho:
        return "area = ",+ (altura**2)
    elif altura != ancho:
        return "perimetro = ",+ altura*2 + ancho*2
print(areaperimeter(4,6))

#%%

    
    







