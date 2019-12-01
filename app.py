from flask import Flask, render_template, request, redirect

from coffee import Menu, db
from coffee.model import menus

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/hello')
@app.route('/hello/<username>')
def sawaddee(username='anonymous'):
    return 'สวัสดีครับ ' + username


# @app.route('/html')
# def test_html():
#     return render_template('base.html')


@app.route('/html')
@app.route('/html/<username>')
def test_html(username='anonymous'):
    return render_template('base.html', page_username=username)


@app.route('/menu')
def menu():
    menus = Menu.select()
    return render_template('menu.html', page_menu=menus)


@app.route('/add_menu', methods=['GET', 'POST'])
def add_menu():
    if request.method == 'POST':
        new_menu = Menu.create(
            coffee_name=request.form["coffee_name"],
            price=request.form["price"]
        )

        new_menu.save()

        return redirect('/menu')

    else:
        return render_template('menu_form.html')


if __name__ == '__main__':
    app.run()
