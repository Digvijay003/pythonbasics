import os
import time

curDir = os.getcwd()
print(curDir)

os.mkdir('newdir3')
time.sleep(2)

os.rename('newdir23','newdirectory')
