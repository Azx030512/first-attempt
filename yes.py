#!python3
import pyinputplus as pyip
while True:
    prompt='Want to know how to keep a person busy for hours?\n'
    response=pyip.inputYesNo(prompt)
    if response == 'no':
        print('Thank you.Have a nice day!')
        break
    if response =='yes':
        continue
    
