import urllib.request
try:
    urllib.request.urlopen("http://pudim.com.br").getcode()
    print('\033[0;32mO pudim está online! \33[m')
except urllib.error.URLError:
    print('\033[0;31mO pudim não está online!\33[m')