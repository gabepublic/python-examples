# convert to XML 
from xml.etree.ElementTree import XML

# assume data is xml
data = "<note><to>Tove</to><from>Jani</from> \
        <heading>Reminder</heading> \
        <body>Don't forget me this weekend!</body></note>"

doc = XML(data)
print(doc)
for el in doc.findall('.//heading'):
    print(el.text)