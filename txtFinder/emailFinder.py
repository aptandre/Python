import pyperclip
import re

#https://automatetheboringstuff.com/files/examplePhoneEmailDirectory.pdf

#names
nameRegex = re.compile(r'(([A-Za-z]+) ([A-Za-z]+) ([a-zA-Z0-9_+.]@+)|(\d+))')
name_list = nameRegex.findall(pyperclip.paste())

#Só faltou dar uma regular expression para organizar os nomes, de resto, está feito!

#get phone numbers
phoneRegex = re.compile('''
\d\d\d #first three digits
-
\d\d\d #Lembre-se que, no caso do Brasil, por exemplo, talvez ocorresse de emitir o ddd (xx)-(xxxxx-xxxx), tendo que separar em grupos e depois colocar tudo em um grupo grandão.
-
\d\d\d\d''', re.VERBOSE)
phone_number_list = phoneRegex.findall(pyperclip.paste())

emailRegex = re.compile('''
[a-zA-Z0-9\-_+.]+ #Pega todos os elementos antes de um @ que ficam entre a-z, A-Z, 0 e 9, \ - + .
@
[a-zA-Z0-9-_+.]+''',re.VERBOSE)
email_list = emailRegex.findall(pyperclip.paste())

for person in range(len(email_list)):
    print(f'{name_list[person][1]} : {email_list[person]} : {phone_number_list[person]}')
#get phone numbers
