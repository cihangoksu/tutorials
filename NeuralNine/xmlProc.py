# %%
from cgitb import handler
import xml.sax

class GroupHandler(xml.sax.ContentHandler):
    def startElement(self, name, attrs):
        print(name)

handler = GroupHandler()
parser = xml.sax.make_parser()
parser.setContentHandler(handler)
parser.parse('data.xml')

# %%
import xml.dom.minidom
domtree = xml.dom.minidom.parse('data.xml')
group = domtree.documentElement

books = group.getElementsByTagName('book')
for book in books:
    print(book.getAttribute('id'))

