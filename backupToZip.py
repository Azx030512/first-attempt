#!python3
# backupToZip.py - Copies an entire  folder and its contents into
# a Zip filewhose filename increments.
import zipfile,os
def backupToZip(folder):
    #Backup the entire contents of "folder" into a ZIP file.
    folder=os.path.abspath(folder)
    #Figure out the filename this code should use base on
    #what files already exist.
    number=1
    while True:
        zipFilename=os.path.basename(folder)+'_'+str(number)+'.zip'
        if not os.path.exists(zipFilename):
            break
        number=number+1
    #Todo:Create the Zip file.
    print(f'Creating  {zipFilename}...')
    backupZip=zipfile.ZipFile(zipFilename,'w')
    

    #Todo:Walk the entire folder tree and compress the files in each folder.
    for foldername,subfolders,filenames in os.walk(folder):
        print(f'Adding files in {foldername}...')
        #Add current folder to the Zip file.
        backupZip.write(foldername)
        for filename in filenames:
            newBase=os.path.basename(folder)+'_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue  #don't backup the backup Zip files
            backupZip.write(os.path.join(foldername,filename))
    backupZip.close()
        

    print('Done')
        
