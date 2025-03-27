import requests
from bs4 import BeautifulSoup
import json
import os
URL='https://en.wikipedia.org/wiki/Lists_of_films'

def get_html(url: str):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0'}
    response = requests.get(url, headers=headers)
    return response.text



def get_films(html):
    soup = BeautifulSoup(html, 'html.parser')
    divs_names = soup.find_all('div', class_='mw-heading mw-heading3')[14:26]
    with open('films_info.txt', 'w', encoding='utf-8') as outfile:
        for i in range(len(divs_names)):
            div_name = soup.find_all('div', class_='mw-heading mw-heading3')[14::1][i].find('h3').text
            list_of_films = soup.find_all('div', class_='mw-heading mw-heading3')[14::1][i].next_sibling.next_sibling
            lis = soup.find_all('div', class_='mw-heading mw-heading3')[14::1][i].next_sibling.next_sibling.find_all(
                'li')
            for li in lis:
                a_tags = li.find_all('a')
                for a_tag in a_tags:
                    text = a_tag.text.strip()  # Получаем текст ссылки
                    link = 'https://en.wikipedia.org' + a_tag.get('href')  # Достаем ссылку
                    part_of_info = f'{text} - {link}'
                    outfile.write(part_of_info)
                    outfile.write('\n')

html = get_html(URL)
get_films(html)
