import requests
from bs4 import BeautifulSoup

page_text = BeautifulSoup(requests.get('https://meduza.io/').text, "html.parser")
my_file = open("lab3_page_text.txt", "w", encoding='utf-8')
my_file.write(page_text.prettify())
my_file.close()
search_tree = page_text.find_all('div', ['Page-section'])
news = []
for i in search_tree:
    elements = i.find_all(['li','div', 'ul', 'article'], [

                                            'PostsListItem PostsListItem--isInPostsListItemHead1to1 PostsListItem--light PostsListItem--index-0 PostsListItem--1to1 PostsListItem--news',
                                            'PostsListItem PostsListItem--isInPostsListItem1to1 PostsListItem--light PostsListItem--index-1 PostsListItem--1to1 PostsListItem--news',
                                            'PostsListItem PostsListItem--isInPostsListItem1to1 PostsListItem--light PostsListItem--index-2 PostsListItem--1to1 PostsListItem--fun',
                                            'PostsListItem PostsListItem--isInPostsListItem1to1 PostsListItem--light PostsListItem--index-3 PostsListItem--1to1 PostsListItem--fun',
                                            'PostsListItem PostsListItem--isInPostsListItem1to1 PostsListItem--light PostsListItem--isLast PostsListItem--index-4 PostsListItem--1to1 PostsListItem--fun',
                                            'PostsListItem PostsListItem--isInPostsListItem1to1 PostsListItem--light PostsListItem--index-3 PostsListItem--1to1 PostsListItem--news',
                                            'PostsListItem PostsListItem--isInPostsListItem1to1 PostsListItem--light PostsListItem--isLast PostsListItem--index-4 PostsListItem--1to1 PostsListItem--news',
                                            'PostsListItem PostsListItem--isInPostsListItemHead1to2 PostsListItem--light PostsListItem--index-0 PostsListItem--1to2 PostsListItem--news',
                                            'PostsListItem PostsListItem--isInPostsListItem1to2 PostsListItem--light PostsListItem--index-1 PostsListItem--1to2 PostsListItem--feature',
                                            'PostsListItem PostsListItem--isInPostsListItem1to1 PostsListItem--light PostsListItem--index-2 PostsListItem--1to1 PostsListItem--feature',
                                            'PostsListItem PostsListItem--isInPostsListItem1to1 PostsListItem--light PostsListItem--index-3 PostsListItem--1to1 PostsListItem--feature',
                                            'PostsListItem PostsListItem--isInPostsListItem1to1 PostsListItem--light PostsListItem--index-1 PostsListItem--1to1 PostsListItem--feature',
                                            'PostsListItem PostsListItem--isInPostsListItemHead1to1 PostsListItem--light PostsListItem--index-0 PostsListItem--1to1 PostsListItem--feature',
                                            'PostsListItem PostsListItem--isInPostsListItem1to1 PostsListItem--light PostsListItem--isLast PostsListItem--index-4 PostsListItem--1to1 PostsListItem--feature',
                                            'PostsListItem PostsListItem--isInPostsListItem1to2 PostsListItem--light PostsListItem--isLast PostsListItem--index-2 PostsListItem--1to2 PostsListItem--feature',
                                            'MediaBlock MediaBlock--fun MediaBlock--1to3 MediaBlock--dark',
                                            'MediaBlock MediaBlock--fun MediaBlock--1to4 MediaBlock--dark',
                                            'MediaBlock MediaBlock--feature MediaBlock--1to3',
                                            'PostsListItem PostsListItem--isInPostsListItem1to1 PostsListItem--light PostsListItem--index-2 PostsListItem--1to1 PostsListItem--news',
                                            'CardBlock CardBlock--1to2',
                                            'MediaBlock MediaBlock--feature MediaBlock--1to3',
                                            'MediaBlock MediaBlock--fun MediaBlock--1to2 MediaBlock--dark',
                                            'MediaBlock MediaBlock--feature MediaBlock--1to2 MediaBlock--dark',
                                            'MediaBlock MediaBlock--feature MediaBlock--1to4',
                                            'PostsListItem PostsListItem--isInPostsListItem1to1 PostsListItem--light PostsListItem--index-1 PostsListItem--1to1 PostsListItem--card',
                                            'PostsListItem PostsListItem--isInPostsListItemHead1to1 PostsListItem--light PostsListItem--index-0 PostsListItem--1to1 PostsListItem--card',
                                            'CardBlock CardBlock--1to3'
                                            ])

    for elem in elements:
        try:
            title = elem.find('span', ['NewsTitle-first NewsTitle-first--feature NewsTitle-first--isInPostsListItem1to2 NewsTitle-first--featured',
                                       'NewsTitle-first NewsTitle-first--news NewsTitle-first--isInPostsListItemHead1to2',
                                       'NewsTitle-first NewsTitle-first--MediaBlock NewsTitle-first--isInMediaBlock1to2',
                                       'NewsTitle-first NewsTitle-first--news NewsTitle-first--isInPostsListItemHead1to1',
                                       'NewsTitle-first NewsTitle-first--news NewsTitle-first--isInPostsListItem1to1',
                                       'NewsTitle-first NewsTitle-first--MediaBlock NewsTitle-first--isInMediaBlock1to2 NewsTitle-first--featured',
                                       'NewsTitle-second NewsTitle-second--MediaBlock NewsTitle-second--isInMediaBlock1to1',
                                       'NewsTitle-first NewsTitle-first--MediaBlock NewsTitle-first--isInMediaBlock1to3 NewsTitle-first--featured',
                                       'NewsTitle-first NewsTitle-first--fun NewsTitle-first--isInPostsListItem1to1',
                                       'NewsTitle-first NewsTitle-first--MediaBlock NewsTitle-first--isInMediaBlock1to3',
                                       'NewsTitle-first NewsTitle-first--CardBlock NewsTitle-first--isInCardBlock1to2',
                                       'NewsTitle-first NewsTitle-first--MediaBlock NewsTitle-first--isInMediaBlock1to4 NewsTitle-first--featured',
                                       'NewsTitle-first NewsTitle-first--card NewsTitle-first--isInPostsListItemHead1to1',
                                       'NewsTitle-first NewsTitle-first--CardBlock NewsTitle-first--isInCardBlock1to3',
                                       'NewsTitle-first NewsTitle-first--MediaBlock NewsTitle-first--isInGames NewsTitle-first--isInMediaBlock1to2 NewsTitle-first--featured',
                                       'NewsTitle-first NewsTitle-first--feature NewsTitle-first--isInPostsListItem1to1 NewsTitle-first--featured',
                                       'NewsTitle-first NewsTitle-first--feature NewsTitle-first--isInPostsListItemHead1to1 NewsTitle-first--featured',
                                       'NewsTitle-first NewsTitle-first--feature NewsTitle-first--isInPostsListItem1to1',
                                       'NewsTitle-first NewsTitle-first--MediaBlock NewsTitle-first--isInMediaBlock1to4'
                                       ]).text
        except AttributeError:
            title = '[без заголовка]'
        try:
            date_created = elem.find('time', {'class':'NewsTime'}).text
        except AttributeError:
            date_created = '[нет даты]'
        try:
            annotation = elem.find('span', ['NewsTitle-second NewsTitle-second--feature NewsTitle-second--isInPostsListItem1to2',
                                         'NewsTitle-second NewsTitle-second--MediaBlock NewsTitle-second--isInMediaBlock1to2',
                                         'NewsTitle-second NewsTitle-second--MediaBlock NewsTitle-second--isInMediaBlock1to3',
                                         'NewsTitle-second NewsTitle-second--feature NewsTitle-second--isInPostsListItem1to1',
                                         'NewsTitle-second NewsTitle-second--feature NewsTitle-second--isInPostsListItemHead1to1',
                                         'NewsTitle-second NewsTitle-second--MediaBlock NewsTitle-second--isInMediaBlock1to4',
                                         'NewsTitle-second NewsTitle-second--MediaBlock NewsTitle-second--isInGames NewsTitle-second--isInMediaBlock1to2'
                                         ]).text
        except AttributeError:
            annotation = '[без аннотации]'

        news.append({
                        'title': title,
                        'date_created': date_created,
                        'annotation': annotation
                     })

for i in range(len(news)):
    print(news[i]['title'])
    print(news[i]['annotation'])
    print(news[i]['date_created'])
    print('\n')
