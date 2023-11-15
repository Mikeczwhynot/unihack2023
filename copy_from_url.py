from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://bioclinica.ro/pentru-pacienti/analize-uzuale/glucoza-semnificatie-si-implicatii"
html = urlopen(url).read()
soup = BeautifulSoup(html, features="html.parser")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.extract()    # rip it out

# get text
text = soup.get_text()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

print(text)

#import urllib.request

#with urllib.request.urlopen("http://www.python.org") as url:
   # s = url.read()
    # I'm guessing this would output the html source code ?
   # print(s)