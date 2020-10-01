import requests
import urllib.request
import time
from bs4 import BeautifulSoup


url = input("Enter Website Url :")
#url = 'http://web.mta.info/developers/turnstile.html'
response = requests.get(url)

### print the response
print(response)

soup = BeautifulSoup(response.text, "html.parser")

# print(soup)

### print all a tag in html
# print(soup.findAll('a'))

# print(soup.find_all('div', attrs={'class': 'crossroad-clients'}))
# divs = soup.find_all('div', attrs={'class': 'crossroad-clients'})[0]

one_a_tag = soup.findAll('a')[36]
link = one_a_tag['href']

# print(link)

downloadurl = 'http://web.mta.info/developers/' + link
urllib.request.urlretrieve(downloadurl, './'+link[link.find('/turnstile_')+1:])
# time.sleep(1)
