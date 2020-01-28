import os,re,sys,shutil

# Using Python external "requests" module to call REST APIs
import requests
import openpyxl
from requests.auth import HTTPBasicAuth
from xml.etree import ElementTree as ET
from openpyxl.drawing.image import Image

filename='config.txt'
templateExcel='template.xlsx'
finalExcel='Finesse.xlsx'
shutil.copy(templateExcel,finalExcel)

wb=openpyxl.load_workbook('Finesse.xlsx')
ws=wb.active
img=Image('DDlogo.png')



ws.add_image (img, 'F1')
wb.save('Finesse.xlsx')
