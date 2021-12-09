#! python3
#examinate the correct date
#P146.7.18.1
import re

def daymonthDetect(i):
    daymonth1Regex=re.compile(r'^\d$')
    if daymonth1Regex.search(i)!=None:
        i='0'+i
        return i
    else:
        return i
dateRegex=re.compile('(\d\d*)/(\d\d*)/(\d\d\d\d)')
print('Please type a date in the form of DD/MM/YYYY')
underdetermine=input()
while dateRegex.search(underdetermine)==None:
    print('Please type as the regular principle1')
    underdetermine=input()
    continue
while dateRegex.search(underdetermine)!=None:
    text1=dateRegex.search(underdetermine)
    text2=[]
    for i in range(1,4):
        text2.append(text1.group(i))
    print(text2)
    day1Regex=re.compile(r'[0-2]\d|3[0-1]')
    text2[0]=daymonthDetect(text2[0])
    text2[1]=daymonthDetect(text2[1])
    print(text2)
    month1Regex=re.compile(r'1([1-2])')
    month2Regex=re.compile(r'0(\d)')
    if month2Regex.search(text2[0])==None or int(text2[0])>31:
        print('There is a  flow.(1)')
        print('Please type again.')
        underdetermine=input()
        continue
    if day1Regex.search(text2[0])==None:
        print('Please type as the regular principle2, there is something wrong in date.')
        underdetermine=input()
        continue
    if month1Regex.search(text2[1])==None and month2Regex.search(text2[1])==None:
        print('Please type as the regular principle3, there is something wrong in month.')
        underdetermine=input()
        continue
    if text2[1]=='02' and int(text2[0])>29:
        print('The date doesn\'t exsit.(1)')
        underdetermine=input()
        continue
    if text2[1] in ['04','06','09','11'] and int(text2[0])>31:
        print('The date doesn\'t exist.(2)')
        underdetermine=input()
        continue
    break

result='/'.join(text2)
print('The reasonable format is underneath:')
print(result)
    

