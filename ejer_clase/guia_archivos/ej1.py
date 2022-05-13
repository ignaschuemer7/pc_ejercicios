
def less(filename):
    with open (filename, 'r') as f:
        for line in f:
          print(line)
def main():
    less('file.txt')

if __name__=='__main__':
    main()