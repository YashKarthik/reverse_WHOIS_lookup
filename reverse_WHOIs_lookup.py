import urllib3
import mechanicalsoup
import webbrowser
import requests
import urllib.parse
from bs4 import BeautifulSoup
import pandas as pd


url=("https://viewdns.info/reversewhois/?")
headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
        'referer':'https://viewdns.info/'
    }

browser = mechanicalsoup.StatefulBrowser()
reg_name = input("enter registrant name")
data = urllib.parse.urlencode({'q': reg_name})
url_n = url + data

browser.open(url_n)
print(browser.get_url())
print(browser.get_current_page())

source = requests.get(url_n).content
df_list = pd.read_html(source)
df = df_list[-1]

print(df)
    
