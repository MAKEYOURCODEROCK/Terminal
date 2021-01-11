import os


os.system('sudo apachectl start')

check = os.path.exists("/opt/homebrew")

os.system('php -S localhost:1515')

#if check == True:
#    os.system('export PATH=/opt/homebrew/bin:$PATH')
    
#else:
#    os.system('/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"')
#    os.system('export PATH=/opt/homebrew/bin:$PATH')
#    os.system('php -S localhost:1515')    
