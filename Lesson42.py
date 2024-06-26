# 22/06/2024

# Шаблонизатор Jinja

from jinja2 import Template


#
# name = "Игорь"
# age = 25
# per = {'name': "Игорь", 'age': 25}
#
# tm = Template("Мне {{ p.age }} лет. Меня зовут {{ p.name }}.")
# # msg = tm.render(n=name, a=age)
# msg = tm.render(p=per)
#
# print(msg)

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def get_name(self):
#         return self.name
#
#
# per = Person('Игорь', 25)
#
# tm = Template("Мне {{ p['age'] }} лет. Меня зовут {{ p.get_name() }}.")
# # msg = tm.render(n=name, a=age)
# msg = tm.render(p=per)
#
# print(msg)

cities = [
    {'id': 1, 'city': 'Москва'},
    {'id': 2, 'city': 'Казань'},
    {'id': 3, 'city': 'Омск'},
    {'id': 4, 'city': 'Ялта'},
    {'id': 5, 'city': 'Воронеж'},
]

link = """<select name="cities">
{% for c in cities %}
{% if c.id >3 -%}
    <option value="{{c ['id'] }}">{{ c['city'] }}</option>
    {%elif c.city == "Москва" %}
    <option>{{ c['city'] }}</option>
    {% else -%}
        {{ c['city'] }}
{%endif%}
{% endfor %}
</select>"""

tm = Template(link)
msg = tm.render(cities=cities)

print(msg)
