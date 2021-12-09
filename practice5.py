name = ''
while not name or not len(name)>2:
    print('Enter your name')
    name = input()
print('Hoe many guests will you have?')
numofguests = int(input())
if numofguests or not numofguests>3:
     print('Be sure to have enough room for all the guests.')
print('Done')



print('what a nice day')
for i in range(5):
    print('I have spent '+str(i)+' day')
input()
