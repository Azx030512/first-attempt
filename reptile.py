#!python3
#reptile.py -- This function can download all the JPG in one page automately
#just input the url as keyword input or select the url and copy it to your clipboard.
import logging,pyperclip,os,bs4,requests,webbrowser,json,re
#logging.disable(logging.CRITICAL)
logging.basicConfig(filename=r'C:\Users\艾\Desktop\practice\errorInfo.txt',level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')

def reptile(url=True):
    os.makedirs(r'C:\Users\艾\Desktop\reptileTarget',exist_ok=True)
    logging.debug('Create the pile target reptile......'+os.path.abspath(r'C:\Users\艾\Desktop\reptileTarget'))
    if url==True:
        url=pyperclip.paste()
    logging.debug('start the reptile to download %s'%url)
    res=requests.get(url)
    res.raise_for_status()
    logging.info(res.text)
    soup=bs4.BeautifulSoup(res.text,'html.parser')   #till here is all the prepare work
    # Here try to select the JPG resources in html element
    JPG_Element=soup.select('img')   #Here is the first try
    if JPG_Element==[]:
        JPG_Element=soup.select('div img')   #Here is the second try
    if JPG_Element==[]:
        # Here we try to solve the problems of content located at javascript data structure
        JPG_regex=re.compile(r'''(window.INIT_DETAIL_CONTENT)(.){1,40}?(\{(.){1,100000}?\})''', re.DOTALL|re.VERBOSE)
        match=JPG_regex.search(res.text)#window.INIT_DETAIL_CONTENT
        jsonData=json.loads(match.group(3))
        new_soup=bs4.BeautifulSoup(jsonData['content'],'html.parser')
        JPG_Element=new_soup.select('img')
    if JPG_Element==[]:
        print('Cannot find the target JPG images')
        logging.error('Cannot find the target JPG images')
        # This means the download has failed
    else :
        numberOpen=len(JPG_Element)
        for i in range(numberOpen):
            JPG_url=JPG_Element[i].get('src')
            if JPG_url[0]!='h':
                JPG_url='http:'+JPG_url
            newName=os.path.basename(JPG_url)
            if len(newName)>50:
                newName=newName[:10]
            if newName[-4]!='.':
                continue
            JPG_file=open(os.path.join(r'C:\Users\艾\Desktop\reptileTarget',newName),'wb')
            logging.info(os.path.join(r'C:\Users\艾\Desktop\reptileTarget',newName))
            JPG_request=requests.get(JPG_url)
            for chunk in JPG_request.iter_content(100000):
                JPG_file.write(chunk)
            JPG_file.close()
            print(f"The NO.%s picture has captured.\nIt has been stored to %s"%(i+1,os.path.join(r'C:\Users\艾\Desktop\reptileTarget',newName)))
        print('sucess !!!')
