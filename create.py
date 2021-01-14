import sys
import time

f= open(sys.argv[1]+'.py',"w+")
f.write("'''\nCreated on \n" + time.ctime(int(time.time())) + "\n@author:abhi\n'''\n")
f.close()
