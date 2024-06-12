import requests
from bs4 import BeautifulSoup


class Parser:
    html = ""
    res = []

    def __init__(self, url, path):
        self.url = url
        self.path = path

    def get_html(self):
        req = requests.get(self.url).text
        self.html = BeautifulSoup(req, "lxml")

    def parsing(self):
        news = self.html.find("ul", class_="law-tree")
        for item in news.find_all('li', class_="gl l2 nost"):
            paragraph = item.text.strip()
            print(paragraph)
            article = item.find_next_sibling('li', class_="st l3").text.strip()
            href = item.find('a').get('href')
            print(article)
            self.res.append({
                "title": paragraph,
                "article": article,
                "href": href
            })

    def save(self):
        with open(self.path, "w") as f:
            i = 1
            for item in self.res:
                f.write(f"Раздел № {i}\n\nГлава: {item['title']}\nСтатья: {item['article']}\nСсылка: {item['href']}"
                        f"\n\n{'*' * 40}\n")
                i += 1

    def run(self):
        self.get_html()
        self.parsing()
        self.save()


def main():
    pars = Parser("https://www.zakonrf.info/uk/?ysclid=lxbf2oag9f389646175", "news.txt")
    pars.run()


if __name__ == '__main__':
    main()
