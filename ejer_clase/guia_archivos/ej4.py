def touch(filename):
    with open(filename,'a') as f:
        f.write("\nhola mundo")
        f.write("\nchau mundo")

def main():
    touch('some.txt')
if __name__=='__main__':
    main()