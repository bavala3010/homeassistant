import requests
from bs4 import BeautifulSoup

login_url = 'https://mobilevikings.be/nl/my-viking/login'
data = {
    'username': 'stockanita@gmail.com',
    'password': '!DTLRdz2AnWrM.G'
}

with requests.Session() as s:
    response = requests.post(login_url , data)
    print(response.text)
    index_page= s.get('http://example.com')
    soup = BeautifulSoup(index_page.text, 'html.parser')
    print(soup.title)