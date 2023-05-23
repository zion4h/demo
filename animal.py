import sys

def cat():
    print('Meow!')
def dog():
    print('Woof!')
def superman():
    print('Hold on!')

def default():
    print('hello')

def main():
    if sys.argv[1] == 'cat':
        cat()
    elif sys.argv[1] == 'dog':
        dog()
    else:
        default()

if __name__ == '__main__':
    main()
