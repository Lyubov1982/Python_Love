# from jinja2 import Environment, FileSystemLoader

# cars = [
#     {'model': 'Audi', 'price': 23000},
#     {'model': 'Skoda', 'price': 17300},
#     {'model': 'Renault', 'price': 44300},
#     {'model': 'Wolksvagen', 'price': 21300}
# ]
# # tpl = "Сумма: {{cs | sum(attribute='price') }}"
# # tpl = "{{ cs | max(attribute='price') }}"
# # tpl = "{{ cs | max(attribute='price').model }}"
# # tpl = "{{ cs | min(attribute='price').model }}"
# # tpl = "{{ cs | random }}"
# tpl = "{{ cs | replace('model', 'brand' }}"
#
# tm = Template(tpl)
# msg = tm.render(cs=cars)
# print(msg)
#
# html = """
# {% macro input_func(name, value, type="text", size=40) %}
#     <input type="{{ type }}" name="{{ name }}" value="{{ value }}" size="{{ size }}" >
# {% endmacro %}
#
# <p> {{ input_func('name', 'Введите имя') }} </p>
# <p> {{ input_func('psw', 'password') }} </p>
# <p> {{ input_func('email', 'электронная почта') }} </p>
# """
#
# tm = Template()
# msg = tm.render()
#
# print(msg)

# from jinja2 import Environment, FileSystemLoader
#
# persons = [
#     {"name": "Алексей", "year": 18, "weight": 78.5},
#     {"name": "Никита", "year": 28, "weight": 82.3},
#     {"name": "Виталий", "year": 33, "weight": 94.0}
# ]
#
# file_loader = FileSystemLoader('templates')
# env = Environment(loader=file_loader)
# # tm = env.get_template('main.html')
# tm = env.get_template('about.html')
# msg = tm.render(users=persons, title="About Jinja")
#
# print(msg)
