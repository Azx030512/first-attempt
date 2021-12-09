#! python3
# searchpypi.py - Opens several search results.
import logging
logging.basicConfig(filename=r'C:\Users\艾\Desktop\practice\errorInfo.txt',level=logging.DEBUG,format=' %(asctime)s - %(levelname)s - %(message)s')
#logging.disable(logging.CRITCAL)

import bs4,webbrowser,os,requests,sys
print('Searching......') #display text while downloading the result page
res=requests.get('https://google.com/search?q='+' '.join(sys.argv[1:]))
res.raise_for_status()

#Retrieve top search result links
soup=bs4.BeautifulSoup(res.text,'html.parser')#establish a soup class for the requests download
linkElement=soup.get('.package-snippet')
#Open a page for every link.
numOpen=min(5,len(linkElement))
for i in range(numOpen):
    urlToOpen='https://'+linkElement[i].get('href')
    print('opening',urlToOpen)
    webbrowser.open(urlToOpen)
