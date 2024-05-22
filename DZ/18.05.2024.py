import json
from random import choice

data = {}


class CountryCapital:
    def __init__(self, country, capital):
        self.country = country
        self.capital = capital
        data[self.country] = self.capital

    def __str__(self):
        return f"{self.country}: {self.capital}"

    @staticmethod
    def add_country(file_name):
        country_name = input("Введите название страны: ")
        capital_name = input("Введите название столицы: ")

        try:
            date = json.load(open(file_name))
        except FileNotFoundError:
            date = {}

        date[country_name] = capital_name

        with open(file_name, 'w') as f:
            json.dump(date, f, indent=2)

    @staticmethod
    def load_from_file(file_name):
        with open(file_name, 'r') as f:
            print(json.load(f))

    @staticmethod
    def delete_country(file_name):
        with open(file_name, 'w') as f:
            json.dump({}, f)  # Записываем пустой словарь в файл
        print("Данные успешно очищены.")

    @staticmethod
    def search_country(file_name):
        country_name = input("Введите название страны для поиска: ")
        try:
            date = json.load(open(file_name))
        except FileNotFoundError:
            date = {}

        if country_name in date:
            print(f"{country_name}: {date[country_name]}")
        else:
            print(f"Страна {country_name} не найдена в списке.")

    @staticmethod
    def edit_country(file_name):
        country_name = input("Введите название страны, которую нужно отредактировать: ")
        new_capital = input("Введите новое название столицы: ")
        try:
            date = json.load(open(file_name))
        except FileNotFoundError:
            date = {}

        if country_name in date:
            data[country_name] = new_capital
            with open(file_name, 'w') as f:
                json.dump(date, f, indent=2)
            print(f"Данные о стране {country_name} обновлены.")
        else:
            print(f"Страна {country_name} не найдена в списке.")


file = "List_capital.json"
index = ""
while index != '6':
    index = input("Выбор данных:\n1-добавление данных\n2-удаление данных\n3-поиск данных\n4-редактирование данных\n5-просмотр данных\n6-завершение работы\nВвод: ")
    if index == "1":
        CountryCapital.add_country(file)
    if index == "5":
        CountryCapital.load_from_file(file)
    if index == "2":
        CountryCapital.delete_country(file)
    if index == "3":
        CountryCapital.search_country(file)
    if index == "4":
        CountryCapital.edit_country(file)
