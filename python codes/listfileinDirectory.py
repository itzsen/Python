import os
import logging
import logging.handlers

import sys


old_stdout = sys.stdout
log_file=open('logmessage.txt','w')
sys.stdout = log_file

print('Senthil')

log_file.close()
sys.stdout=old_stdout

print('Senthil is a dummy')

old_stdout = sys.stdout
log_file=open('logmessage.txt','a')
sys.stdout = log_file

print('Senthil rocks')

log_file.close()
sys.stdout=old_stdout

