def head(filename,num_lines):
    with open(filename,'r') as f:
        for i in range(num_lines):
            print(f.readline())
def main():
    head('file.txt',2)

if __name__=='__main__':
    main()