from bs4 import BeautifulSoup
import requests

URL = "https://samples.vx-underground.org/samples/Families/"


def get7zFromLink(link):
    if '.pdf' in link:
        return
    if '.7z' not in link:
        try:
            r = requests.get(link)
        except requests.exceptions.RequestException:
            return

        rSoup = BeautifulSoup(r.content, "html5lib")

        links = rSoup.find_all('a', href=True)
        for link in links:
            if 'http' in link['href']:
                get7zFromLink(link['href'])
    else:
        family = ''
        link = link.split('/')
        virus_hash = link[len(link) - 1]
        virus_hash = virus_hash.split('.')
        virus_hash = virus_hash[0]
        i = 0
        while i < len(link):
            if link[i] == 'Families':
                family = link[i + 1]
            i = i + 1

        requests.post('http://127.0.0.1:8000/insert_virus/' + virus_hash + '/' + family)


if __name__ == '__main__':
    get7zFromLink(URL)
