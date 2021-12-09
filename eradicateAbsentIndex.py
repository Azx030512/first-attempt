#!python3
#eradicateAbsentIndex.exe -- This function can organize the number of a string of files
import os,shutil,re,logging
logging.basicConfig(level=logging.DEBUG,filename=r'C:\Users\艾\Desktop\practice\errorInfo.txt',format=' %(asctime)s - %(levelname)s - %(message)s ')
from pathlib import Path
targetlist=[]
def eradicateAbsentIndex(folder):
    regex=re.compile(r"""
    (capitalsquiz_answers)
    (\d*)
    (.txt)
    """,re.VERBOSE)
    number=1
    folder=os.path.abspath(folder)
    for filename in os.listdir(folder):
        mo=regex.search(filename)
        logging.info(filename)
        if mo==None:
            continue
        else:
            if(mo.group(3)==str(number)):
                number+=1
                continue
            else:
                newname=mo.group(1)+str(number)+mo.group(3)
                logging.info(os.path.join(folder,filename)+' and '+os.path.join(folder,newname))
                shutil.move(os.path.join(folder,filename),os.path.join(folder,newname))
                number+=1

                
        
