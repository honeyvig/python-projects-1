# -*- coding: utf-8 -*-

import requests
from lxml import html
from urllib.request import Request, urlopen
from getpass import getpass

login_url = "https://auth.tdameritrade.com/auth?response_type=code&client_id=TDARETAILWEB%40AMER.OAUTHAP&redirec"

#--http://kazuar.github.io/scraping-tutorial/
userName = getpass( 'Username: ' )
password = getpass( 'Password: ' )

session_requests = requests.session()

result = session_requests.get(login_url)
tree = html.fromstring(result.text)
authenticity_token = list(set(tree.xpath("//input[@name='_csrf']/@value")))[0]

print(result)

payload = {
	"su_username": "userName", 
	"su_password": "password", 
	"_csrf": "authenticity_token"
}

result = session_requests.post(
	login_url, 
	data = payload, 
	headers = dict(referer=login_url)
)

print(result)