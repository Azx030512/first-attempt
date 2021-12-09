#!python3
import os,shutil
from pathlib import Path
for i in range(0,10):
    fatherPath=Path.cwd()
    print('Please input the date in the format like MMDDYYYY')
    date=input()
    item=date[0]+date[1]+'-'+date[2]+date[3]+'-'+date[4]+date[5]+date[6]+date[7]
    exampleFile=open(fatherPath/f'{item}.docx','w')
    exampleFile.write("What a brilliant creation !")
    exampleFile.close()
