import requests
from bs4 import BeautifulSoup

url='https://www.example.com/'
response = requests.get(url)

soup=BeautifulSoup(response.text,'html.parser')

print(soup.prettify())

# Extracting title

title=soup.title.text
print(title)

# Extracting Links

for link in soup.find_all('a'):
    print(link.get('href'))

# Extracting Paragraph

paragraphs=soup.find('p').text.split('\n')
print(paragraphs)

#Extract Data Using css selector

header=soup.select('h1')
for h in header:
    print(h.text)















