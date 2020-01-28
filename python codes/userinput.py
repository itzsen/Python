filename='config.txt'
fileopen=open(filename,'w')
print('What is the IP address?')
ip='ip:'+input()+'\n'
print('What is the Username?')
username='username:'+input()+'\n'
print('What is the Password?')
password='password:'+input()+'\n'
print(ip)
print(username)
print(password)
fileopen.write(ip)
fileopen.write(username)
fileopen.write(password)
fileopen.close()
