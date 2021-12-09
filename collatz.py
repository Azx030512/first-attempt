import sys
def collatz(number2):
    try:
        while True:
            5/(number2-1)
            if number2%2==0:
                number2=number2//2
                print(number2)
            elif number2%2==1:
                number2=number2*3+1
                print(number2)
    except:
        sys.exit()
number2=int(input())
collatz(number2)
