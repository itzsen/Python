import re

filename='config.txt'

fileopen=open(filename)
contents=fileopen.read()
fileopen.close()
print('File is already there. Here are the contents')
print(contents)


ipRegex=re.compile(r'(ip:)(.*)')
userRegex=re.compile(r'(username:)(.*)')
passRegex=re.compile(r'(password:)(.*)')
findip=ipRegex.search(contents)
finduser=userRegex.search(contents)
findpass=passRegex.search(contents)
ip=findip.group(2)
username=finduser.group(2)
password=findpass.group(2)

print(ip)
print(username)
print(password)
