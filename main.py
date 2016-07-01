import requests
from bs4 import BeautifulSoup

hrefSet = set()

def forum_spider(max_pages):
    page = 1
    while page < max_pages:
        url = 'https://thenewboston.com/forum/recent_activity.php?page=' + str(page)
        source_code = requests.get(url).text
        # plain_text = source_code.text
        soup = BeautifulSoup(source_code, 'html.parser')
        for link in soup.findAll('a', {'class': 'title text-semibold'}):
            href = link.get('href')
            title = link.string
            formattedTitle = title.strip()
            # print(href)
            print('\nTitle: ', formattedTitle, '\n')
            print('Posters:\n'),
            get_single_item_data(href)
        page += 1
        print("\npage:", page - 1)

def get_single_item_data(item_url):
    source_code = requests.get(item_url).text
    soup = BeautifulSoup(source_code, 'html.parser')
    for posters in soup.findAll('a', {'class': 'user-name'}):
        username = posters.string
        formattedUsername = username.strip()
        print(formattedUsername)
    for link in soup.findAll('a'):
        href = link.get('href')
        hrefSet.add(href)
    print(hrefSet)


forum_spider(2)