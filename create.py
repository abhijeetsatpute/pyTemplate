import sys
import time
AUTHOR = 'abhi'

f= open(sys.argv[1]+'.py',"w+")
f.write("'''\nCreated on \n" + time.ctime(int(time.time())) + "\n@author: " + AUTHOR + "\n'''\n")
f.close()
