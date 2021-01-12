import wget
import getpass
import ssl
import os
os.system('export SSL_CERT_DIR=/etc/ssl/certs')
username = getpass.getuser()

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://www.python.org/static/img/python-logo@2x.png"

wget.download(url, '/users/' + username)
os.system('pip3 install requests')
os.system('pip3 install json')
os.system('pip3 install pickle')
os.system('pip3 install code')
os.system('pip3 install getpass')
os.system('pip3 install subprocess')
os.system('pip3 install sys')
os.system('pip3 install colorama')
os.system('pip3 install datetime')
