import requests
import openpyxl
from openpyxl.drawing.image import Image
from openpyxl.styles import PatternFill,Border,Fill
from requests.auth import HTTPBasicAuth
from xml.etree import ElementTree as ET
from lxml import etree



filename='XMLconfig.txt'
#templateExcel='template.xlsx'
#finalExcel='Finesse.xlsx'
#shutil.copy(templateExcel,finalExcel)




root = etree.Element('SystemConfig')
root.append(etree.Element('uri'))
#root.append(child)

s=etree.tostring(root,pretty_print=True)


fileopen=open(filename,'w')

 fileopen.write(s)

 fileopen.close()
