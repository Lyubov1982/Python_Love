import requests
from bs4 import BeautifulSoup
import re
import csv


def get_html(url):
    r = requests.get(url)
    return r.text


def write_csv(data):
    with open("plugins.csv", "a") as f:
        writer = csv.writer(f, lineterminator="\r", delimiter=";")
        writer.writerow([data])


def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    p1 = soup.find("div", class_="content__text")
    if p1:
        paragraphs = p1.find_all("p")
        for paragraph in paragraphs:
            text = paragraph.get_text(strip=True)
            print(text)
            write_csv(text)


def main():
    url = "https://www.livemaster.ru/topic/1390403-100-knig-kotorye-dolzhen-prochest-kazhdyj"
    get_data(get_html(url))


if __name__ == '__main__':
    main()
