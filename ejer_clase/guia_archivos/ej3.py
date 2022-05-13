
def tail(filename,n):
    with open(filename,'r') as f:
        x=f.readlines()
    ultimos_n=x[len(x)-n:len(x)]
    print(ultimos_n)

def main ():
    tail('file.txt',3)

if __name__=='__main__':
    main()