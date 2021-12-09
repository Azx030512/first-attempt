print('please type out your math score on the screen')

sc=int(input())
if sc>=60:
    print('great')
    if sc>=80 and sc<=100:
        print('brilliant')
    else:
        print('incredible')

else:
    print('bad')
print('That is all')
print('type Alice')
name=input()
if name =='Alice':
    print('Hi,Alice')
else:
    print('Hello,stranger')
print('What is your age?')
age=int(input())
if age >=20:
    print('all right')
elif age <=18:
    print('You are not Alice,kiddo.')
input()
