import re
import requests


def find_emails(page):
    page_text = requests.get(page).text
    all_emails = re.findall(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9_.+-]+\.[a-zA-Z0-9_.+-]+', page_text)
    unique_list = []
    for i in all_emails:
        if i not in unique_list:
            unique_list.append(i)
    print(unique_list)


find_emails('http://www.tsu.ru/help/contacts.php/')
