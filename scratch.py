import bs4
import requests

url = 'http://www.yahoo.co.jp'
param = {}
proxies = {
    'http':'127.0.0.1:8080',
    'https':'127.0.0.1:8080'
}
#auth = HTTPAuth()
headers = {'User-Agent': 'Sample Header', 'contents-type':'application-json'}

r = requests.get(url = url)
#r = requests.get(url = url, proxies = proxies, auth = auth)

if r.status_code != requests.codes.ok:
    print('Error')
    exit(1)
soup = bs4.BeautifulSoup(r.content,"html.parser")