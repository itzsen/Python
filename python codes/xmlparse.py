import xml.etree.ElementTree as ET

tree= ET.parse('systemconfig.xml')
root = tree.getroot()
for child in root:
    if child.tag=='uri':
        uri=child.text
    else:
        for element in child:
            if element.tag=='backupHost':
                backupHost=element.text
            elif element.tag=='backupPort':
                backupPort=element.text
            elif element.tag=='host':
                host=element.text
            elif element.tag=='peripheralId':
                peripheralId=element.text
            elif element.tag=='port':
                port=element.text

print(uri,host,port,backupHost, backupPort,peripheralId)

wb=openpyxl.load_workbook('Finesse.xlsx')
sheet=wb.get_sheet_by_name('Sheet1')
sheet['B20']=host
sheet['B21']=port
sheet['B22']=backupHost
sheet['B23']=backupPort
sheet['B24']=peripheralId
sheet['B25']=uri
wb.save('Finesse.xlsx')

