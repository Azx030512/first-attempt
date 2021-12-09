#!python3
# copyImages.exe -- This function copy all the images from one director to another director
# the connector is the two address
def copyImages(folder,destination):
    import re,os,shutil
    from pathlib import Path
    exampleRegex=re.compile(r'^IMG(.*)\.jpg$')
    folder=os.path.abspath(folder)
    for images in os.listdir(folder):
        print(images)
        mo=exampleRegex.search(images)
        if mo==None:
            continue
        else:
            print('success')
            shutil.copy(folder+'\\'+images,destination)
        
