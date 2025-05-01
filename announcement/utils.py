import requests
from bs4 import BeautifulSoup
from django.conf import settings


def get_response(url):
    response = requests.get(url)
    return response.text

def parser_text(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    div_lists = soup.find_all("div", class_='item product_listbox oh')
    items_list = []
    for item in div_lists:
        link = settings.MAIN_LINK + item.find("a")['href']
        soup_2 = BeautifulSoup(get_response(link), 'html.parser')
        article = soup_2.find("strong").get_text()
        items_list.append(
            {"title": item.find("strong").get_text(),
             "link": link,
             "description": item.find("div", class_="product_text pull-left").
                 get_text(strip=True).replace("\xa0", ""),
             "price": item.find("div", class_='listbox_price text-center').
                 get_text(strip=True).replace(" сом", ""),
             "article": article
             }
        )

    return items_list


def result_parse(sub_category: str) -> list:
    html_text = get_response(settings.MAIN_LINK + "/" + sub_category)
    result = parser_text(html_text)
    return result

