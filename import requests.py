import requests
from bs4 import BeautifulSoup

loginurl = ('https://edi.evc-net.com/')
secure_url = ('https://edi.evc-net.com/Transactions/List')

payload = {
    'emailField': 'bartland@gmail.com',
    'passwordField': '!Hu2Su5!@WTyzh',
    'Login': 'Aanmelden'
}

with requests.session() as s:
     s.post(loginurl, data=payload)
     r = s.get(secure_url)
     soup = BeautifulSoup(r.content, 'html.parser')
     print(soup.prettify())

