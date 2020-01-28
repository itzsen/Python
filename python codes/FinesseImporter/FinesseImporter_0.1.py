import requests
import openpyxl
from openpyxl.drawing.image import Image
from openpyxl.styles import PatternFill,Border,Fill
from requests.auth import HTTPBasicAuth
from xml.etree import ElementTree as ET
import logging
import logging.handlers
import os,re,sys,shutil


def printRESTAPIResponse(prefix='printRESTAPIResponse()', response=''):
    """
        Print the REST API response with the HTTP Request status code
        and the Response body text
    """
    print (prefix + " - Status: ", response.status_code) # This is the http request status
    print (prefix + " - Text: ", response.text)
    print ("\n")


def PUT(url, username, password, params='', data=''):
    """
        Call the PUT HTTP Request using HTTP Basic Auth authentication
        
        Parameters:
            url (str): The URL to make the REST request
            username (str): The username of the user making the HTTP request
            password (str): The password of the user making the HTTP request
            params(dictionary, optional): Dictionary or bytes to be sent in the query string for the Request.
                                          (e.g. {"category" : "NOT_READY"})
            data(str, optional): The HTTP request body as a string

        Returns: Response object (http://docs.python-requests.org/en/master/api/#requests.Response) - The HTTP Response as a result of the HTTP Request
    """
    print ("Executing PUT '%s'\n" % url)
    try:
        headers = {'Content-Type': 'application/xml'}
        print ("PUT() data: %s\n" % data)
        response = requests.put(url=url, auth=HTTPBasicAuth(username, password), headers=headers, params=params, data=data)
        printRESTAPIResponse("PUT()", response)
        return(response)
    except:
       print ("An error occured in the PUT request to %s" % url)
       print (sys.exc_info());
       sys.exit()

def POST(url, username, password, params='', data=''):
    """
        Call the POST HTTP Request using HTTP Basic Auth authentication
        
        Parameters:
            url (str): The URL to make the REST request
            username (str): The username of the user making the HTTP request
            password (str): The password of the user making the HTTP request
            params(dictionary, optional): Dictionary or bytes to be sent in the query string for the Request.
                                          (e.g. {"category" : "NOT_READY"})
            data(str, optional): The HTTP request body as a string

        Returns: Response object (http://docs.python-requests.org/en/master/api/#requests.Response) - The HTTP Response as a result of the HTTP Request
    """
    print ("Executing POST '%s'\n" % url)
    try:
        headers = {'Content-Type': 'application/xml'}
        print ("POST() data: %s\n" % data)
        response = requests.post(url=url, auth=HTTPBasicAuth(username, password), headers=headers, params=params, data=data)
        printRESTAPIResponse("POST()", response)
        return(response)
    except:
       print ("An error occured in the POST request to %s" % url)
       print (sys.exc_info());
       sys.exit()

def DELETE(url, username, password):
    """
        Call the DELETE HTTP Request using HTTP Basic Auth authentication
        
        Parameters:
            url (str): The URL to make the REST request
            username (str): The username of the user making the HTTP request
            password (str): The password of the user making the HTTP request

        Returns: Response object (http://docs.python-requests.org/en/master/api/#requests.Response) - The HTTP Response as a result of the HTTP Request
    """
    print ("Executing DELETE '%s'\n" % url)
    try:
        response = requests.delete(url=url, auth=HTTPBasicAuth(username, password))
        printRESTAPIResponse("DELETE()", response)
        return(response)
    except:
       print ("An error occured in the DELETE request to %s" % url)
       print (sys.exc_info());
       sys.exit()


filename='config.txt'
templateExcel='Finesse.xlsx'
finalExcel='FinesseImport.xlsx'
shutil.copy(templateExcel,finalExcel)

if os.path.isfile(filename):
    fileopen=open(filename)
    contents=fileopen.read()
    fileopen.close()
    ipRegex=re.compile(r'(ip:)(.*)')
    userRegex=re.compile(r'(username:)(.*)')
    passRegex=re.compile(r'(password:)(.*)')
    findip=ipRegex.search(contents)
    finduser=userRegex.search(contents)
    findpass=passRegex.search(contents)
    ip=findip.group(2)
    username=finduser.group(2)
    password=findpass.group(2)
else:
    fileopen=open(filename,'w')
    print('Config file does not exist. New config file created.')
    print('What is the Finesse FQDN address?')
    ip=input()
    newip='ip:'+ip+'\n'
    print('What is the Username?')
    username=input()
    newusername='username:'+username+'\n'
    print('What is the Password?')
    password=input()
    newpassword='password:'+password+'\n'
    fileopen.write(newip)
    fileopen.write(newusername)
    fileopen.write(newpassword)
    fileopen.close()
    
