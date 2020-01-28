import paramiko
client=paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
com="show version"
client.connect('10.2.2.51','22', username='ucadmin', password='Syr!nx2112')
output=""
stdin, stdout, stderr = client.exec_command(com)

print ('ssh succuessful. Closing connection')
stdout=stdout.readlines()
client.close()
print ('Connection closed')

print (stdout)
print (com)
for line in stdout:
    output=output+line
if output!="":
    print (output)
else:
    print ('There was no output for this command')
