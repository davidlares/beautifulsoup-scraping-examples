import urllib.request as request
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import os

# verify https existance
print("HTTPS EXISTANCE")
print("=================================")
req = request.Request('http://python.org')
result = request.urlopen(req)
print(result.geturl())
print(" ")

# site weight
print("SITE WEIGHT")
print("=================================")
url = "https://python.org"
site = request.urlopen(url)
meta = site.info()
print("Content-Length (kbs): ", site.headers['content-length'])
print(" ")

# real site weight (disk)
print("REAL SITE WEIGHT")
print("=================================")
f = open('out.txt','r')
print("File on disk: ", len(f.read()))
f.close()

f = open('out.txt','wb')
f.write(site.read())
site.close()
f.close()

f = open('out.txt','r')
print("File on disk after download: ", len(f.read()))
f.close()
print('os.stat().st_size returns: ', os.stat('out.txt').st_size)
print(" ")

# check www url existance
print("WWW URL EXISTANCE")
print("=================================")
req = request.Request('http://python.org')
res = request.urlopen(req)
print("Check www: ", res.geturl())
print(" ")

# check meta description < 150 chars
print("CHECK IF META IS BELOW 150 CHARS")
print("=================================")
site = request.urlopen('http://python.org')
soup = BeautifulSoup(site,features="html.parser")
description = soup.find('meta', attrs = {'name': 'description'})
print("Meta description size: ", len(description.get('content')))
if(len(description.get('content')) < 150):
	print("Description is lower than standard")
print(" ")

# check title
print("WEBSITE TITLE")
print("=================================")

html = request.urlopen('http://python.org')
soup = BeautifulSoup(html.read(),features="html.parser")
print("Title size is: ", len(soup.html.head.title.string))
print("Title: ", soup.html.head.title.string)
print(" ")

# keywords
print("WEBSITE KEYWORDS")
print("=================================")
site = request.urlopen('http://python.org')
soup = BeautifulSoup(site,features="html.parser")
keywords = soup.find('meta', attrs = {'name': 'keywords'})
print("Python.org Keywords: ", keywords.get('content'))
words = keywords.get('content').split()
print("WORD LIST")
for word in words:
	print(word, len(soup.findAll(text = re.compile(word))))
print(" ")

# image
print("WEBSITE LOGO/IMAGE URL")
print("=================================")
site = request.urlopen('http://python.org')
soup = BeautifulSoup(site,features="html.parser")
count = 1
for image in soup.findAll('img'):
	print('Image #{}', count, ": ", image["src"])
	count += 1
print(" ")

# h1 headings
print("H1 HEADINGS COUNTERS")
print("=================================")
site = request.urlopen('http://python.org')
soup = BeautifulSoup(site,features="html.parser")
for h1 in soup.find_all('h1'):
	print("h1 element: ", h1)
print('Total (h1s): ', len(soup.find_all('h1')))
print(" ")

# links lists
print("LINKS LIST") 
print("=================================")
site = request.urlopen('http://python.org')
soup = BeautifulSoup(site,features="html.parser")
links = []

# getting links
elements = soup.select('a')
for element in elements:
	link = element.get('href')
	if link.startswith('http'):
		links.append(link) # inserting into a list 
print(links)
print(" ")
# checking the url and http status code
for link in links[:10]: 
	crequest = urlopen(link)
	print("Link: ", link, "Response: ", crequest.code)
print(" ")

print("ANALYTICS CHECKER")
print("=================================")
# google analytics
site = request.urlopen('http://python.org')
soup = BeautifulSoup(site, features="html.parser")
if soup.findAll(text = re.compile('.google-analytics')):
	print('Site have Google Analytics')
else:
	print('Do not have Google Analytics')
print(" ")