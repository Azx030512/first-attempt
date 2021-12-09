import time,sys
indent = 0
indentIncreasing = True
try:
    while True:
        print('  '*indent,end='')
        print('********')
        time.sleep(0.1)#Pause for 0.1 in a second
        #indentIncreasing=True
        if indentIncreasing:
            indent = indent + 1
            if indent == 20 :
                indentIncreasing = False
        else:
            indent=indent - 1
            if indent == 0:
               indentIncreasing = True
except KeyboardInterrupt:
    sys.exit()
