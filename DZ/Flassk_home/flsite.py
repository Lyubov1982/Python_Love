from flask import Flask, render_template, request, flash, url_for, session, redirect, abort

app = Flask(__name__)
app.config["SECRET_KEY"] = 'ee915954c301efa240899dc7c6181f4ca8311df0'

menu = [
    {'name': 'Установка', 'url': 'index'},
    {'name': 'Первое приложение', 'url': 'about'},
    {'name': 'Обратная связь', 'url': 'contact'},
    {'name': 'Авторизация', 'url': 'login'},
]


@app.route('/')
@app.route('/index')
def index():
    print(url_for('index'))
    return render_template('index.html', menu=menu)


@app.route('/about')
def about():
    print(url_for('about'))
    return render_template('about.html', title="О сайте", menu=menu)


@app.route('/contact', methods=["POST", "GET"])
def contact():
    if request.method == 'POST':
        if len(request.form['username']) > 2:
            flash('Сообщение отправлено', category='success')
        else:
            flash('Ошибка отправки', category='error')
    return render_template('contact.html', title="Обратная связь", menu=menu)


@app.route("/profile/<username>")
def profile(username):
    if 'userLogged' not in session or session['userLogged'] != username:
        abort(401)

    return f"Профиль пользователя: {username}"


@app.route("/login", methods=["POST", "GET"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    elif request.method == 'POST' and request.form['username'] == "selfedu" and request.form['psw'] == '123':
        session['userLogged'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogged']))
    return render_template('login.html', title="Авторизация", menu=menu)


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page404.html', title="Страница не найдена", menu=menu)


# with app.test_request_context():
#     print(url_for('about'))

if __name__ == '__main__':
    app.run(debug=True)
