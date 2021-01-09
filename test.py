import subprocess

import sys
#mport os


#user = input("Blu-1.1$ ")

#if user[0:3] == "ls ":
#    print("hi")

#user = user[3:]


#ls = os.listdir(user)
#x = len(ls)

#y = 0

#while y != x:
#    print(ls[y])
#    y += 1    

p = subprocess.Popen([sys.executable, 'more/server/server.py'], 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.STDOUT)

hi = input("hi")
if hi == "hi":
    print("hello")