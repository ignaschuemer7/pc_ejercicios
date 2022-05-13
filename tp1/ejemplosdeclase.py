def millas():
    nombre=input("bienvenido, ingrese su nombre ")
    millas=int(input("ingrese las millas "))
    print(millas,"millas, equivalen a",millas*1.609344,"kilometros")
millas()

#%%
def positividad(numero):
    if numero>0:
        print("el numero",numero,"es positivo \n")
    else:
        print("el numero",numero,"es negativo \n")
positividad(7)
#%%
def inscripcion(n):
    terminacion = n % 10
    if terminacion==0 :
        return "lunes"
    elif terminacion<4 :
        return "martes"
    elif terminacion<7 :
        return "miercoles"  
    else:
        return "jueves"
print(inscripcion(72387849))
#%%
def promedio (nombre,parcial,tps):
    r=[]
    notas=0
    for i in range(len(nombre)):
        for x in range(len(tps)):
            notas+=tps[i][x]
        promedio = (notas+parcial[i]) / 4
        if promedio >=4 :
            r.extend([nombre[i],promedio])
        notas=0
    return r
print(promedio(["igna","julian","pato"],[10,6,9],[(3,4,10),(3,1,2),(7,8,3)]))

#%%
#dni_mask
def dni_mask(dni,bloque=(1,2,3),mask="-"):
     salida=""
     while True:
         try:
             if len(dni)!=8:
                 raise ValueError
             elif dni.isnum():
                 break
         except ValueError:
             dni=(int(input("ingrese un nuevo dni")))
     dni=list(dni)
     
     
         
     
