def cubomascercano(n):
    y,x=n,n
    if (n**(1/3)) == int(n**(1/3)):
        return n
    else:
        while y**(1/3) != int(y**(1/3)):    
            y+=1 
        while x**(1/3) != int (x**(1/3)):
            x-=1
        if abs(n-y) > abs(n-x):
           return x
        else:
           return y     
print("el cubo mas cercano es",cubomascercano(int(input("ingrese un numero entero: "))))
            
