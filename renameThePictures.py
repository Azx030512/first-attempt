#!python
#renameThePictures -- just for convenience
import os,shutil
index=1
for filename in os.listdir(r'C:\Users\艾\Desktop\Adobe Premiere Pro Audio Previews\定点延时摄影'):
    newname='IMG'+str(index)+'.jpg'
    index+=1
    absWorkingDir=r'C:\Users\艾\Desktop\Adobe Premiere Pro Audio Previews\定点延时摄影'
    filename=os.path.join(absWorkingDir,filename)
    newname=os.path.join(absWorkingDir,newname)
    print(f'Rename "{filename}" to "{newname}"  ***')
    shutil.move(filename,newname)
