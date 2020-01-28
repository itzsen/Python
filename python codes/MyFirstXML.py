import xml.etree.ElementTree as xml

def GenerateXML1(fileName):
    root=xml.Element("SystemConfig")
    uri=xml.Element("uri")
    uri.text="/finesse/api/SystemConfig"
    root.append(uri)
    cti=xml.Element("cti")
    root.append(cti)
    host=xml.SubElement(cti,"host")
    host.text="1.1.1.1"
    port=xml.SubElement(cti,"port")
    port.text="42027"
    backupHost=xml.SubElement(cti,"backupHost")
    backupHost.text="2.2.2.2"
    backupPort=xml.SubElement(cti,"backupPort")
    backupPort.text="43027"
    peripheralId=xml.SubElement(cti,"peripheralId")
    peripheralId.text="43027"
    secure=xml.SubElement(cti,"secure")
    secure.text="false"

    tree=xml.ElementTree(root)

    with open(fileName,"wb") as files:
        tree.write(files)


def GenerateXML2(fileName):
    root=xml.Element("ClusterConfig")
    uri=xml.Element("uri")
    uri.text="/finesse/api/ClusterConfig"
    root.append(uri)
    secondaryNode=xml.Element("secondaryNode")
    root.append(secondaryNode)
    host=xml.SubElement(secondaryNode,"host")
    host.text="1.1.1.1"

    tree=xml.ElementTree(root)

    with open(fileName,"wb") as files:
        tree.write(files)


def GenerateXML3(fileName):
    root=xml.Element("EnterpriseDatabaseConfig")
    uri=xml.Element("uri")
    uri.text="/finesse/api/EnterpriseDatabaseConfig"
    root.append(uri)
    host=xml.Element("host")
    host.text="1.1.1.1"
    root.append(host)
    backupHost=xml.Element("backupHost")
    backupHost.text="1.1.1.2"
    root.append(backupHost)
    port=xml.Element("port")
    port.text="1433"
    root.append(port)
    databaseName=xml.Element("databaseName")
    databaseName.text="customer_awdb"
    root.append(databaseName)
    domain=xml.Element("domain")
    domain.text="example.com"
    root.append(domain)
    username=xml.Element("username")
    username.text="Admin"
    root.append(username)
    password=xml.Element("password")
    password.text="password"
    root.append(password)
    tree=xml.ElementTree(root)

    with open(fileName,"wb") as files:
        tree.write(files)
        
if __name__=="__main__":
    GenerateXML1("SystemConfig.xml")
    GenerateXML2("ClusterConfig.xml")
    GenerateXML3("EnterpriseDatabaseConfig.xml")
