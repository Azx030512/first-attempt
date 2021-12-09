def hello():
    print('Howdy!')
    print('Howdy!!!')
    print('Hello there.')
hello()
hello()
hello()


def hello(name):
    print('Hello , '+name)
hello('Alice')
hello('Bob')


def sayHello(name):
    print('Hello '+name)
sayHello('Ai')


import random,time
def getAnswer(answerNumber):
    if answerNumber == 1:
        return'It is certain'
    elif answerNumber == 2:
        return'It is decidedly so'
    elif answerNumber == 3:
        return'Yes'
    elif answerNumber == 4:
        return'Reply hazy try again.'
    elif answerNumber == 5:
        return'Ask again later'
    elif answerNumber == 6:
        return'Concentrate and ask again'
    elif answerNumber == 7:
        return'My reply is no'
    elif answerNumber == 8:
        return'Outlook not so good'
    elif answerNumber == 9:
        return'Very doubtful'
#r=random.randint(1,9)
#fortune = getAnswer(r)
while True:
    r=random.randint(1,9)
    fortune = getAnswer(r)
    print(fortune)
    time.sleep(0.2)
    


def a():
    print('a() starts')
    b()
    d()
    print('a() returns')
def b():
    print('b() starts')
    c()
    print('b() returns')
def c():
    print('c() starts')
    print('c() returns')
def d():
    print('d() starts')
    print('d() returns')
a()


#def spam():
    #eggs = '31337'
#spam()
#print(eggs)


def spam():
    eggs=99
    bacon()
    print(eggs)
def bacon():
    ham=101
    eggs=0
    print(eggs)
spam()


def spam():
    print(eggs)
eggs=99
spam()


def spam():
    eggs='spam local'
    print(eggs)
def bacon():
    eggs='bacon local'
    print(eggs)
    spam()
    print(eggs)
eggs='global'
bacon()
print(eggs)

def spam():
     global eggs
     eggs='spam'
eggs='global'
spam()
print(eggs)


def spam():
    global eggs
    eggs='spam'
def bacon():
    eggs='bacon'
    print(eggs)
def ham():
    print(eggs)
eggs=42
spam()
print(eggs)
bacon()


def spam():
    print(eggs)
   #eggs='spam local'
eggs='global'
spam()

def spam(devideBy):
    try:
        return 42/devideBy
    except :
        print('Error : Invalid argument')
print(spam(2))
print(spam(12))
print(spam(0))
print(spam(1))
