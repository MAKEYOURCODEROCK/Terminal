#!/usr/bin/env
import requests
import json
import pickle
import code
import os
import getpass
import subprocess
import sys

from colorama import init
init()
from colorama import Fore, Back, Style


import datetime
version = "1.1"

#space
print()
#space


def download_file(url, filename=''):
    try:
        if filename:
            pass            
        else:
            filename = req.url[downloadUrl.rfind('/')+1:]
 
        with requests.get(url) as req:
            with open(filename, 'wb') as f:
                for chunk in req.iter_content(chunk_size=8192):
                    if chunk:
                        f.write(chunk)
            return filename
    except Exception as e:
        print(e)
        return None



def paskeys():
    filecheck = os.path.exists("more/data/paskeys.json")
    if filecheck == True:
        with open('more/data/paskeys.json') as f:
            dataa = json.load(f)

        pwdchk = getpass.getpass("Enter Password: Secure 1.0$ ")
        if pwdchk == dataa['pwd']:
            print()
            print(Fore.GREEN + "Welcome Back")
            print(Style.RESET_ALL)
        else:
            print(Fore.RED + "Incorrect")
            paskeys()


        
paskeys()



now = datetime.datetime.now()
print("Blu Lanuched On:")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
print("--version--" + version)
print('To Quit Type "Quit" Or "Q"')
print('For Help Ask "Info"')

def inputs(version):
    user_input = input("Blu-" + version + "$ ")
    arguments(user_input)
    


def arguments(user_input):
    location = './'
    username = getpass.getuser()

    if user_input == "":
        inputs(version)
    
    if user_input == "info":
        print()
        print("Welcome To Blu")
        print("Here You Are Welcome To Download Almost Anything")
        inputs(version)

    if user_input == "Quit" or user_input == "quit" or user_input == "QUIT" or user_input == "q" or user_input == "Q" or user_input == "exit" or user_input == "EXIT":
        data = {}
        data['path'] = "./"
        writeToJSONFile('','var/path',data)
        print("Bye!!")
        now = datetime.datetime.now()
        print("Blu Closed On:")
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        print(Fore.GREEN + "[Process Completed]")
        quit()

    if user_input == "keys":
        print("Keys-Are:")
        inputs(version)

    if user_input[0:3] == "ssh":
        os.system(user_input)
        inputs(version)


    if user_input[0:12] == "blu install " or user_input[0:12] == "BLU INSTALL " or user_input[0:12] == "blu install":
        print("Pkg installer 0.0.1")
        pkg = user_input[12:]

        if pkg == "":
            user_input = "info"
            arguments(user_input)

        if pkg == "brew" or pkg == "homebrew":
            op = os.name
            if op == "posix":
                os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
                os.system('export PATH=/opt/homebrew/bin:$PATH')
                print("Brew Installed")
            else:
                print("Homebrew cannot download on your device")
            inputs(version)

        print("Intall Package Not Found")
        inputs(version)


    if user_input == "sudo service apache2 start" or user_input == "sudo apache start" or user_input == "start webserver":
        print("Starting Web Server")
        p = subprocess.Popen([sys.executable, 'more/server/launch.py'], 
                                    stdout=subprocess.PIPE, 
                                    stderr=subprocess.STDOUT)
        print("WebServer Is Online On localhost and localhost:1515")
        print("Launching PHP")
        print("Launchihng MYSQL")
        print("Launching PHPMYADMIN")
        inputs(version)


    if user_input == "kill servers" or user_input == "killall -9 php":
        os.system('killall -9 php')
        inputs(version)


    if user_input[0:4] == "sudo":
        os.system(user_input)

    if user_input[0:3] == "npm":
        os.system(user_input)

    if user_input[0:4] == "pip3" or user_input[0:3] == "pip":
        os.system(user_input)

    if user_input == "python3" or user_input[0:3] == "python":
        os.system(user_input)
        inputs(version)

    if user_input[0:7] == "python3":
        os.system(user_input)
        inputs(version)


    if user_input[0:3] == "rm " or user_input[0:3] == "RM " or user_input[0:3] == "Rm " or user_input[0:3] == "rM ":
        with open('var/path.json') as y:
            location = json.load(y)

        path = user_input[3:]
        os.remove(location['path'] + '/' + path) 
        inputs(version)


    if user_input[0:4] == "brew":
        os.system('export PATH=/opt/homebrew/bin:$PATH')
        os.system(user_input)
        inputs(version)


    if user_input == "bash":
        os.system('bash')
        inputs(version)

    if user_input == "zsh":
        os.system('zsh')
        inputs(version)

    if user_input == "sh":
        os.system('sh')
        inputs(version)


    if user_input == "bash":
        os.system('bash')
        inputs(version)

    if user_input == "csh":
        os.system('csh')
        inputs(version)

    if user_input == "ksh":
        os.system('ksh')
        inputs(version)

    if user_input == "dash":
        os.system('dash')
        inputs(version)

    if user_input[0:3] == "cd " or user_input[0:3] == "CD " or user_input[0:3] == "Cd " or user_input[0:3] == "cD ":
        with open('var/path.json') as l:
            low = json.load(l)
        pathcheck = os.path.exists(low['path'] + user_input[3:] + '/')
        if pathcheck == True:
            with open('var/path.json') as v:
                low = json.load(v)
            location = {}
            location['path'] = low['path'] + user_input[3:] + '/'
            writeToJSONFile('','var/path', location)
            inputs(version)
        elif user_input != "cd ..":
            print("No Such File Or Directory")
            inputs(version)
        else:
            with open('var/path.json') as v:
                low = json.load(v)
            location = {}
            location['path'] = low['path'] + user_input[3:] + '/'
            writeToJSONFile('','var/path', location)
            inputs(version)

    if user_input[0:3] == "ls" or user_input[0:3] == "LS" or user_input[0:3] == "Ls" or user_input[0:3] == "lS":
        with open('/users/' + username + '/var/path.json') as z:
            location = json.load(z)

        ls = os.listdir(location['path'])
        x = len(ls)
        y = 0

        while y != x:
            print(ls[y])
            y += 1    

        inputs(version)

    

    

    if user_input == "sudo install blu.js" or user_input == "npm install blu.js" or user_input == "sudo install blu_js" or user_input == "npm install blu_js":
        download_file('http://bluhorse.ca/cdn/blu.js.zip', 'more/library/blu.js.zip')
        inputs(version)

    if user_input == "playarea" or user_input == "-pa-" or user_input == "PlayArea":
        print("Welcome To Play Area")
        while True:
            ii = input("PlayArea$ ") 

            if ii == "q" or ii == "quit":
                inputs(version)


    if user_input == "secure document" or user_input == "encrypted document" or user_input == "-sd-" or user_input == "-ed-":
        print("Making Files")
        filecheck = os.path.exists("more/data/secure$_docs.json")
        filecheck2 = os.path.exists("more/data/more_secure$_docs.json")
        if filecheck == False:
            doc_input = {}
            doc_input['Secure_Docs_1'] = input("Secure_Docs-1.0$ ")
            writeToJSONFile('','more/data/secure$_docs',doc_input)
            inputs(version)
        elif filecheck2 == False:
            doc_input = {}
            doc_input['Secure_Docs_2'] = input("Secure_Docs-1.0$ ")
            writeToJSONFile('','more/data/more_secure$_docs',doc_input)
            inputs(version)
        else:
            doc_input = {}
            doc_input['Secure_Docs_3'] = input("Secure_Docs-1.0$ ")
            writeToJSONFile('','more/data/evenmore_secure$_docs',doc_input)
            inputs(version)

    if user_input == "-gsd-" or user_input == "-ged-" or user_input == "get secure document" or user_input == "get encrypted document":
        checkfiles = os.path.exists("more/data/secure$_docs.json")
        if checkfiles == True:
        
            filecheck = os.path.exists("more/data/paskeys.json")
            if filecheck == True:
                with open('more/data/paskeys.json') as f:
                    dataa = json.load(f)

                pwdchk = getpass.getpass("Enter Password: Secure 1.0$ ")
                if pwdchk == dataa['pwd']:
                    print()
                    print(Fore.GREEN + "Here are your documents:")
                    print(Style.RESET_ALL)
                else:
                    print(Fore.RED + "Incorrect")
                    arguments(user_input)


            with open('more/data/secure$_docs.json') as a:
                ged = json.load(a)

            print(ged['Secure_Docs_1'])
            print()

            with open('more/data/more_secure$_docs.json') as b:
                gsd = json.load(b)

            print(gsd['Secure_Docs_2'])
            print()

            with open('more/data/evenmore_secure$_docs.json') as c:
                gett = json.load(c)

            print(gett['Secure_Docs_3'])
            print()

            inputs(version)
        else:
            print("You Don't Have Any Docs")
            inputs(version)

        

    if user_input == "-dp-" or user_input == "delete password" or user_input == "DELETE PASSWORD":
        filecheck = os.path.exists("more/data/paskeys.json")
        if filecheck == True:
            dp = getpass.getpass("To Make Changes Enter Password")
            with open('more/data/paskeys.json') as f:
                dataa = json.load(f)
            if dp == dataa['pwd']:
                if os.path.exists("more/data/paskeys.json"):
                    os.remove("more/data/paskeys.json") 
                    inputs(version)
        else:
            print("You Dont Have A Password")
            inputs(version)

    if user_input == "-cp-" or user_input == "change password" or user_input == "Change Password" or user_input == "CHANGE PASSWORD":
        filecheck = os.path.exists("more/data/paskeys.json")
        if filecheck == False:
            print("You Don't Have A Password")
        else:
            pwdint = getpass.getpass("Enter Old Password")
            with open('more/data/paskeys.json') as f:
                dataa = json.load(f)
            if pwdint == dataa['pwd']:
                data = {}
                data['pwd'] = getpass.getpass("Set New Password $ ")
                writeToJSONFile('','more/data/paskeys',data)
                inputs(version)
            else:
                print("Incorrect")
                inputs(version)


    if user_input == "-sp-" or user_input == "set password" or user_input == "Set Pwd" or user_input == "set pwd" or user_input == "Set Password" or user_input == "SET PASSWORD":
        filecheck = os.path.exists("more/data/paskeys.json")
        if filecheck == False:
            data = {}
            data['pwd'] = getpass.getpass("Set Password $ ")
            writeToJSONFile('','more/data/paskeys',data)
            inputs(version)
        else:
            print("You Already Have A Password")
            inputs(version)

    if user_input == "time" or user_input == "Time" or user_input == "TIME":
        now = datetime.datetime.now()
        print (now.strftime("%Y-%m-%d %H:%M:%S"))
        inputs(version)

    if user_input == "text" or user_input == "editor" or user_input == "Text" or user_input == "TEXT":
        os.system('python3 more/code.py')
        print("Your Back!!")
        inputs(version)

    if user_input == "calculator" or user_input == "-c-" or user_input == "Calculator" or user_input == "CALCULATOR":
        while True:
            num1 = input("Calculator 1.0$ ")

            check = num1.isnumeric()

            while check == False:
                if num1 == "":
                    break

                if num1 == "q" or num1 == "quit" or num1 == "Quit" or num1 == "QUIT" or num1 == "Q":
                    break
                    
                print("Error Bad Input")
                num1 = input("Calculator 1.0$ ")
                check = num1.isnumeric()

            while num1 == "":
                num1 = input("Calculator 1.0$ ")

            if num1 == "done" or num1 == "q" or num1 == "quit":
                inputs(version)
                exit()

            num1 = int(num1)

            

            

            

            op = input("Calculator 1.0$ ")

            while op != "x" or op != "+" or op != "/" or op != "-" or op != "÷":
                if op == "":
                    break
                if op == "x" or op == "+" or op == "/" or op == "-" or op == "÷":
                    break
                if op == "q" or op == "quit" or op == "Quit" or op == "QUIT" or op == "Q":
                    break
                print("Error Bad Operator")
                op = input("Calculator 1.0$ ")

            while op == "":
                op = input("Calculator 1.0$ ")

            if op == "done" or op == "q" or op == "quit":
                inputs(version)
                exit()

            num2 = input("Calculator 1.0$ ")

            check2 = num2.isnumeric()

            while check2 == False:
                if num2 == "":
                    break

                if num2 == "q" or op == "quit" or op == "Quit" or op == "QUIT" or op == "Q":
                    break
                
                print("Error Bad Input")
                num2 = input("Calculator 1.0$ ")
                check = num2.isnumeric()

            while num2 == "":
                num2 = input("Calculator 1.0$ ")

            if num2 == "done" or num2 == "q" or num2 == "quit":
                inputs(version)
                exit()


            num2 = int(num2)

            if op == "x":
                print(num1 * num2)
                inputs(version)
                exit()
            elif op == "+":
                print(num1 + num2)
                inputs(version)
                exit()
            elif op == "/" or op == "÷":
                print(num1 / num2)
                inputs(version)
                exit()
            elif op == "-":
                print(num1 - num2)
                inputs(version)
                exit()
            

            
        


    if user_input == "Amitoj":
        print("You Have Found The Secret Name Of Whom Made This BootLeg Bash")
        inputs(version)

    if user_input == "download":
        print("Download What?")
        print("  You Can Say:")
        print("   download Os")
        print("   download speech")
        print("   download tutorial")
        print("   download speech-to-text")
        print("   and much more")
        inputs(version)

    if user_input == "clear" or user_input == "bye" or user_input == "CLEAR" or user_input == "BYE" or user_input == "Clear" or user_input == "Bye":
        os.system('clear')
        inputs(version)

    print("Command Not Found")
    inputs(version)



def writeToJSONFile(path, fileName, data):
    filePathNameWExt = './' + path + '/' + fileName + '.json'
    with open(filePathNameWExt, 'w') as fp:
        json.dump(data, fp)


inputs(version)
