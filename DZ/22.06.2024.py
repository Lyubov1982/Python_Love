from jinja2 import Template

lists = [
    {'a href': 'index', 'menu': 'Главная'},
    {'a href': 'news', 'menu': 'Новости'},
    {'a href': 'about', 'menu': 'О компании'},
    {'a href': 'shop', 'menu': 'Магазин'},
    {'a href': 'contacts', 'menu': 'Контакты'},
]

link = """<ul name="lists">
{% for l in lists %}
    <li> <a href="/{{l ['a href'] }} {% if l['a href'] == 'index' %}class="activ">{{ l['menu'] }}</a></li>
{% else %}">{{ l['menu'] }}</a></li>
{% endif %}
{%endfor%}
</ul>"""

tm = Template(link)
msg = tm.render(lists=lists)

print(msg)
