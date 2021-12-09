#!python3
#renameDates.py - Renames filenames with American MM-DD-YYYY date format
#to European DD-MM-YYYY
import shutil,os,re,send2trash
from pathlib import Path
# Create a regex that matches files with the American date format
datePattern=re.compile(r"""(.*?)              #all text before the date
((0|1)?\d)-                                     #one or two digits for the month
((0|1|2|3)?\d)-                              #one or two digits for the day
((\d\d)\d*)                                       #four digits for the year
(.*?)$""",re.VERBOSE)                           #all text after the date

#Todo : Loop over the files in the working directory.
for amerFilename in os.listdir('.'):
    print(amerFilename)
    mo=datePattern.search(amerFilename)

#Todo : Skip the files without a date.
    if mo==None:
        continue

#Todo : Get the different parts of the filename.
    print('a')
    beforePart=mo.group(1)
    monthPart=mo.group(2)
    dayPart=mo.group(4)
    yearPart=mo.group(6)
    afterPart=mo.group(8)

#Todo : Form the European-style filename.
    euroFilename=beforePart+dayPart+'-'+monthPart+'-'+yearPart+afterPart

#Todo : Get the full,absolute file paths.
    absWorkingDir=os.path.abspath('.')
    amerFilename=os.path.join(absWorkingDir,amerFilename)
    euroFilename=os.path.join(absWorkingDir,euroFilename)

#Unlink the privious files
    #send2trash.send2trash(euroFilename)

#Todo : Rename the files.
    print(f'Renaming "{amerFilename}" to "{euroFilename}"...')
    shutil.move(amerFilename,euroFilename)
    #uncomment after testing
