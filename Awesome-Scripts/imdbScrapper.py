import urllib
from bs4 import BeautifulSoup

print ("Collecting data from IMDb charts....\n\n\n")
print ("The current top 15 IMDB movies are the following: \n\n")
response = urllib.request.urlopen("http://www.imdb.com/chart/top")
html = response.read()
soup = BeautifulSoup(html, 'html.parser')
mytd = soup.findAll("td", {"class":"titleColumn"})
for titles in mytd[:15]:
    print (titles.find('a').text)
print ("\n\nThank you for using IMDB script ...")
