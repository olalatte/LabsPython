import re
import requests


def find_emails(page):
    addresses = {
             q
             for gr_1 in range(len(page))
             for text in requests.get(page[gr_1]).text.split(' ')
             for q in re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9_.+-]+\.[a-zA-Z0-9_.+-]+', text)
            }
    my_file = open("lab2_email_addresses.txt", "w", encoding='utf-8')
    my_file.write('\n'.join(addresses))
    my_file.close()
    return addresses


def find_links(new_links, unique_links):

    page_text = requests.get(new_links[0]).text
    my_file = open("page_text.txt", "w", encoding='utf-8')
    my_file.write(page_text)
    my_file.close()
    links = [
             lin
             for i in range(len(new_links))
             for text in requests.get(new_links[i]).text.split(' ')
             for lin in re.findall('href="/.+/"', text)
            ]
    links = {
                'https://www.sibur.ru' + links[i][6:len(links[i]) - 1]
                if links[i][6] == '/'
                else links[i][6:len(links[i]) - 1]
                for i in range(len(links))
            }
    new_links = [x for x in links if x not in unique_links]
    for x in links:
        if x not in unique_links:
            unique_links.append(x)
            print(x)
    print(len(new_links))

    if len(new_links) > 0:
        find_links(new_links, unique_links)
    else:
        my_file = open("all_links.txt", "w", encoding='utf-8')
        my_file.write('\n'.join(unique_links))
        my_file.close()
    return unique_links


def find_links2(new_links, unique_links):

    page_text = requests.get(new_links[0]).text
    my_file = open("page_text.txt", "w", encoding='utf-8')
    my_file.write(page_text)
    my_file.close()
    links = [
             lin
             for i in range(len(new_links))
             for text in requests.get(new_links[i]).text.split(' ')
             for lin in re.findall(r'href="(?!mailto:)(?:)(https?:\/\/?\w+\.sibur\.ru[^"]*)"', text)
            ]
    new_links = [x for x in links if x not in unique_links]
    for x in links:
        if x not in unique_links:
            unique_links.append(x)
            print(x)
    print(len(new_links))

    if len(new_links) > 0:
        find_links2(new_links, unique_links)
    else:
        my_file = open("all_links2.txt", "w", encoding='utf-8')
        my_file.write('\n'.join(unique_links))
        my_file.close()
    return unique_links


slash_links = find_links(new_links=['https://www.sibur.ru/'], unique_links=['https://www.sibur.ru/'])
intern_links = find_links2(new_links=['https://www.sibur.ru/'], unique_links=['https://www.sibur.ru/'])
all_links = intern_links + slash_links
all_emails = find_emails(all_links)

print('Всего кол-во ссылок: '+str(len(all_links)))
print('Всего кол-во адресов: '+str(len(all_emails)))
