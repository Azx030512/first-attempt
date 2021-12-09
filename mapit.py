#!python3
# mapit.py -- Launches a map in the browser using an address from the
# command line or clipboard

import webbrowser,sys,pyperclip
if len(sys.argv)>1:
    #get address from command line.
    address=' '.join(sys.argv[1:])
else:
    #Todo:get address from clipboard
    address=pyperclip.paste()
webbrowser.open(r'https://www.google.com.hk/maps/place/'+address)
