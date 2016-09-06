from UN_XML_Directory import xml_directory
import glob
import xml.etree.ElementTree as ET

en_xml_files = glob.glob1(xml_directory, "*en.xml")

column_names = []

for f in en_xml_files:
    tree = ET.parse(xml_directory + f)
    root = tree.getroot()
    for child in root:
        #print('Column Name: {0} \tValue:{1}'.format(child.get('name'), child.text))
        column_names.append(child.get('name'))

i = 1

for column in sorted(set(column_names)):
    print('{0})\t{1}'.format(i, column))
    i += 1
