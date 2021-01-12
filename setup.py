import wget
import getpass
import ssl
import os
os.system('export SSL_CERT_DIR=/etc/ssl/certs')
username = getpass.getuser()

ssl._create_default_https_context = ssl._create_unverified_context

url = "https://raw.githubusercontent.com/MAKEYOURCODEROCK/Terminal/Download-1.1/main.py"

wget.download(url, 'C:/users/' + username)

os.mkdir('more')

urltwo = "https://raw.githubusercontent.com/MAKEYOURCODEROCK/Terminal/Download-1.1/more/code.py"

wget.download(urltwo, 'C:/users/' + username + '/' + 'more/')

urlthree = "https://raw.githubusercontent.com/MAKEYOURCODEROCK/Terminal/Download-1.1/more/games.py"

wget.download(urlthree, '/users/' + username + '/' + 'more/')

os.mkdir('more/server')

urlfour = "https://raw.githubusercontent.com/MAKEYOURCODEROCK/Terminal/Download-1.1/more/server/launch.py"

wget.download(urlfour, 'C:/users/' + username + '/' + 'more/server/')

urlfive = "https://github.com/MAKEYOURCODEROCK/Terminal/blob/Download-1.1/more/server/server.py"

wget.download(urlfive, 'C:/users/' + username + '/' + 'more/server/')

os.mkdir('var')

urlsix = "https://raw.githubusercontent.com/MAKEYOURCODEROCK/Terminal/Download-1.1/var/path.json"

wget.download(urlsix, 'C:/users/' + username + '/' + 'var')

os.mkdir('var/www')

urlel = "https://raw.githubusercontent.com/MAKEYOURCODEROCK/Terminal/Download-1.1/var/www/readme.md"

wget.download(urlel, 'C:/users/' + username + '/' + 'var/www')

urlseven = "https://raw.githubusercontent.com/MAKEYOURCODEROCK/Terminal/Download-1.1/var/www/.server.py"

wget.download(urlseven, 'C:/users/' + username + '/' + 'var/www')

os.mkdir('var/www/html')

urleight = "https://raw.githubusercontent.com/MAKEYOURCODEROCK/Terminal/Download-1.1/var/www/html/index.html"

wget.download(urleight, 'C:/users/' + username + '/' + 'var/www/html')


urlnine = "https://raw.githubusercontent.com/MAKEYOURCODEROCK/Terminal/Download-1.1/var/www/html/main.php"

wget.download(urlnine, 'C:/users/' + username + '/' + 'var/www/html')

urlten = "https://raw.githubusercontent.com/MAKEYOURCODEROCK/Terminal/Download-1.1/var/www/html/readme.md"

wget.download(urlten, 'C:/users/' + username + '/' + 'var/www/html')

os.system('pip3 install requests')
os.system('pip3 install json')
os.system('pip3 install pickle')
os.system('pip3 install code')
os.system('pip3 install getpass')
os.system('pip3 install subprocess')
os.system('pip3 install sys')
os.system('pip3 install colorama')
os.system('pip3 install datetime')
