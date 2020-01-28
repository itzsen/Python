import xml.etree.ElementTree as ET

tree= ET.parse('systeminfo.xml')
root = tree.getroot()
for child in root:
    if child.tag=='currentTimestamp':
        currentTimestamp=child.text
    elif child.tag=='deploymentType':
        deploymentType=child.text
    elif child.tag=='lastCTIHeartbeatStatus':
        lastCTIHeartbeatStatus=child.text
    elif child.tag=='license':
        license1=child.text
    elif child.tag=='peripheralId':
        peripheralId=child.text
    elif child.tag=='status':
        status=child.text
    elif child.tag=='statusReason':
        statusReason=child.text
    elif child.tag=='systemAuthMode':
        systemAuthMode=child.text
    elif child.tag=='timezoneOffset':
        timezoneOffset=child.text
    elif child.tag=='uri':
        uri=child.text
    elif child.tag=='xmppDomain':
        xmppDomain=child.text
    elif child.tag=='xmppPubSubDomain':
        xmppPubSubDomain=child.text
    elif child.tag=='primaryNode':
        for element in child:
            primaryNode=element.text
    elif child.tag=='secondaryNode':
        for element in child:
            secondaryNode=element.text

wb=openpyxl.load_workbook('Finesse.xlsx')
sheet=wb.get_sheet_by_name('Sheet1')
sheet['B6']=currentTimestamp
sheet['B7']=deploymentType
sheet['B8']=lastCTIHeartbeatStatus
sheet['B9']=license1
sheet['B10']=peripheralId
sheet['B11']=primaryNode
sheet['B12']=secondaryNode
sheet['B13']=status
sheet['B14']=statusReason
sheet['B15']=systemAuthMode
sheet['B16']=timezoneOffset
sheet['B17']=xmppDomain
sheet['B17']=xmppPubSubDomain
sheet['B19']=uri
wb.save('Finesse.xlsx')

'''
