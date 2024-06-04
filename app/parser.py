from bs4 import BeautifulSoup
import requests
from random import randint
from app.handlers import imageslist
import urllib3
def parsing():
    urllib3.disable_warnings()
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36 OPR/85.0.4341.60'
        }
    url = 'https://ru.freepik.com/free-photos-vectors/motivation/' + str(randint(1, 100)) + '#uuid=6e83ad0c-97a3-4a90-86b8-38f657612b69'
    page = requests.get(url, headers=headers, verify = False)
    print(page.status_code)
    soup = BeautifulSoup(page.content, 'html.parser')
    img = soup.findAll('a', class_ = 'showcase__link js-detail-data-link')
    for pic in img:
        url = pic.find("img").get("data-src")
        imageslist(url)