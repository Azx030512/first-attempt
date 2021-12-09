total = 0
for num in range(101):
    total = total+num
print(total)



print('My name is')
for i in range(5):
    print('Jimmy Five Times ('+str(i)+')')



print('My name is')
i=0
while i<5:
    print('Jimmy Five Times ('+ str(i)+')')
    i=i+1


for i in range(12 , 16):
    print(i)
for i in range(12,20,3):
    print(i)


for i in range(10,-5,-2):
    print(i)


import random
for i in range(10):
    print(random.randint(1,10))
    print('('+str(i)+')')


from random import *
for i in range(10):
    print(randint(1,10))
    print('('+str(i)+')')
input()
