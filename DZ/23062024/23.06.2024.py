from jinja2 import Environment, FileSystemLoader

lists = [
    {'type': 'text', 'name': 'firstname', 'placeholder': 'Имя'},
    {'type': 'text', 'name': 'lastname', 'placeholder': 'Фамилия'},
    {'type': 'text', 'name': 'address', 'placeholder': 'Адрес'},
    {'type': 'tel', 'name': 'phone', 'placeholder': 'Телефон'},
    {'type': 'email', 'name': 'email', 'placeholder': 'Почта'},
]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)
tm = env.get_template('index.html')
msg = tm.render(users=lists)

print(msg)
