#!python3
import pyinputplus as pyip
print("what would you like to have as bread?")
bread=pyip.inputMenu(['wheat','white','sourDough'])
print("which kind of  protein do you prefer?")
protein=pyip.inputMenu(['chicken','turkey','ham','tofu'])
print("Would you like some cheese?")
cheeseAnswer=pyip.inputYesNo()
print("Would you need some mayo,mustard,lettuce,tomato")
choice=pyip.inputMenu(['mayo','mustard','lettuce','tomato','no'])
print("How many sandwiches do you want?")
number=pyip.inputNum(min=1)
