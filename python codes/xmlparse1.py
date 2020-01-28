import xml.etree.ElementTree as ET

tree= ET.parse('enterprisedatabaseconfig.xml')
root = tree.getroot()
for child in root:
    if child.tag=='uri':
        uri=child.text
    elif child.tag=='backupHost':
        backupHost=child.text
    elif child.tag=='host':
        host=child.text
    elif child.tag=='databaseName':
        databaseName=child.text
    elif child.tag=='port':
        port=child.text
    elif child.tag=='password':
        password=child.text
    elif child.tag=='username':
        username=child.text

print(uri,host,port,backupHost, databaseName,username,password)
'''


wb=openpyxl.load_workbook('Finesse.xlsx')
sheet=wb.get_sheet_by_name('Sheet1')
sheet['B32']=host
sheet['B33']=backupHost
sheet['B34']=databaseName
sheet['B35']=port
sheet['B36']=username
sheet['B37']=password
sheet['B38']=uri
wb.save('Finesse.xlsx')

'''
