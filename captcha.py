import base64
from bs4 import BeautifulSoup as BSHTML
import urllib.request
import pytesseract

page = urllib.request.urlopen('http://challenge01.root-me.org/programmation/ch8/')
soup = BSHTML(page, "html.parser")
images = soup.findAll('img')
for image in images:
    image = image['src'].split(",")[1]
bytes = image.encode('utf-8')
print(bytes)
with open('imageToSave.png', "wb") as handler:
    handler.write(base64.decodebytes(bytes))
text = pytesseract.image_to_string('imageToSave.png')
print(text[:-1])


